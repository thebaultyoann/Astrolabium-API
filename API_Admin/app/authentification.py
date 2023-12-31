from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from typing import Annotated
from jose import JWTError, jwt  
from app.db import get_db_UserAdmin
import app.crud as crud
import app.schema as schema
import sys
import pyotp

sys.path.append('../../files/')
from variable import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_ADMIN_EXPIRE_MINUTES

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_twofa(twofa_code:str, key):
    totp = pyotp.TOTP(key)
    return totp.now()==twofa_code

def authenticate_user_admin(db: Session, username: str, password: str, twofa_code :str):
    try:
        user = crud.get_user_admin(db, username)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"bug in authenticate_user_admin {user}",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not user:
        return False
    if not verify_password(password, user.password_hashed):
        return False
    try :
        if not verify_twofa(twofa_code=twofa_code, key=user.twofa_key):
            return False
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"wrong here {user.twofa_key}{twofa_code} ",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

#Authentification functions
async def get_current_admin_user(token: Annotated[str, Depends(oauth2_scheme)], db:Session = Depends(get_db_UserAdmin)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schema.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = crud.get_user_admin(db=db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

def login_the_user_admin_for_access_token(form_data, form_twofa, db):
    #try:
    user = authenticate_user_admin(db=db, username=form_data.username, password=form_data.password, twofa_code=form_twofa.twofa_code)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_ADMIN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
