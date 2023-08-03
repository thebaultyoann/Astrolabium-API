from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from typing import Annotated
from jose import JWTError, jwt  
from app.db import get_db_Users, get_db_UserAdmin
import app.crud as crud
import app.schema as schema
import sys
import pyotp

sys.path.append('../../files/')
from variable import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, ACCESS_TOKEN_ADMIN_EXPIRE_MINUTES

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_twofa(twofa_code:str, key):
    totp = pyotp.TOTP(key)
    return totp.now()==twofa_code

def authenticate_user(db: Session, username: str, password: str):
    user = crud.get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.password_hashed):
        return False
    return user

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

def change_password(old_plain_password:str, new_password_hashed:str, username:str, db:Session):
    user = crud.get_user(db,username)
    if not user:
        return False
    if not verify_password(old_plain_password,user.password_hashed):
        return False
    if crud.change_user_password(db, username, new_password_hashed):
        return True
    return False

#Authentification functions 
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db:Session = Depends(get_db_Users)):
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
    user = crud.get_user(db=db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(
    current_user: Annotated[schema.User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

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

def manage_password_changement(current_user,password_form,db):
    if password_form.new_password_plain == password_form.new_password_confirmation_plain:
        new_password_hash = get_password_hash(password_form.new_password_plain)
        if change_password(old_plain_password=password_form.old_password_plain, db=db, username=current_user.username, new_password_hashed=new_password_hash):
            return "Your password has been successfully changed"
        return "Incorrect old password"
    return "Passwords do not match"

def login_the_user_for_access_token(form_data,db):
    try:
        user = authenticate_user(db, form_data.username, form_data.password)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

def login_the_user_admin_for_access_token(form_data, form_twofa, db):
    #try:
    user = authenticate_user_admin(db=db, username=form_data.username, password=form_data.password, twofa_code=form_twofa.twofa_code)
    #except:
    #    raise HTTPException(
    #        status_code=status.HTTP_401_UNAUTHORIZED,
    #        detail="Incorrect username or password - except",
    #        headers={"WWW-Authenticate": "Bearer"},
    #    )
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

def get_admin(db:Session =Depends(get_db_UserAdmin)):
    user = crud.get_admin(db=db)
    return user