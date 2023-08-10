from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date
from passlib.context import CryptContext
from sqlalchemy.orm import sessionmaker, Session, declarative_base

import sys

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

root_password = sys.argv[1] if len(sys.argv) > 1 else None  
mariadb_ip = sys.argv[2] if len(sys.argv) > 2 else None 
username = sys.argv[3] if len(sys.argv) > 3 else None  
password = sys.argv[4] if len(sys.argv) > 4 else None
twofa_key = sys.argv[5] if len(sys.argv) > 5 else None    

engine = create_engine("mariadb+mariadbconnector://root:"+root_password+"@"+mariadb_ip+":3306/espf_users")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class UserAdmin(Base):
    __tablename__ = 'useradmin'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(4),  unique=True, index=True)
    password_hashed = Column(String(60))
    twofa_key = Column(String(32))

def add_user(session: Session, username, password, twofa_key):
    password = get_password_hash(password)
    new_user = UserAdmin(username=username, password_hashed=password, twofa_key=twofa_key)
    try:
        session.add(new_user)
        session.commit()
    except:
        return False
    return True

if add_user(session, username, password, twofa_key):
    print("Admin_user for API added")
else:
    print("Error in the admission of API admin_user")

