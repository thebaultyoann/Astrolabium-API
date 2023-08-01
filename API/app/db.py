from sqlalchemy import create_engine,Column, Integer, Date, JSON, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../../files/')
from variable import DB_Username_API, DB_Password_API, DB_Username_APIAdmin, DB_Password_APIAdmin, DB_Username_Users,DB_Password_Users,DB_Username_UserAdmin,DB_Password_UserAdmin,DB_Container_Name, DB_Name_For_Api_Tables, DB_Name_For_Users_Tables


engineAPI = create_engine("mariadb+mariadbconnector://"+DB_Username_API+":"+DB_Password_API+"@"+DB_Container_Name+":3306/"+DB_Name_For_Api_Tables)
engineAPIAdmin= create_engine("mariadb+mariadbconnector://"+DB_Username_APIAdmin+":"+DB_Password_APIAdmin+"@"+DB_Container_Name+":3306/"+DB_Name_For_Api_Tables)
engineUsers = create_engine("mariadb+mariadbconnector://"+DB_Username_Users+":"+DB_Password_Users+"@"+DB_Container_Name+":3306/"+DB_Name_For_Users_Tables)
engineUserAdmin = create_engine("mariadb+mariadbconnector://"+DB_Username_UserAdmin+":"+DB_Password_UserAdmin+"@"+DB_Container_Name+":3306/"+DB_Name_For_Users_Tables)

Base = declarative_base()
Base2 = declarative_base()
Base3 = declarative_base()

class DataDay(Base):
    __tablename__ = 'dataday'
    id = Column(Integer, primary_key=True)
    simulationDate = Column(Date)
    sample = Column(Integer)
    targetDays = Column(JSON)

class Users(Base2):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(4),  unique=True, index=True)
    password_hashed = Column(String(60))
    disabled = Column(Boolean, default=True)

class UserAdmin(Base3):
    __tablename__ = 'useradmin'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(4),  unique=True, index=True)
    password_hashed = Column(String(60))

SessionLocalAPI = sessionmaker(autocommit=False, autoflush=False, bind=engineAPI)
SessionLocalAPIAdmin = sessionmaker(autocommit=False, autoflush=False, bind=engineAPIAdmin)
SessionLocalUsers = sessionmaker(autoflush=False, class_=Users)
SessionLocalUsersAdmin = sessionmaker(autoflush=False, class_=UserAdmin)


#Dependency
def get_db_API():
    db = SessionLocalAPI()
    try:    
        yield db
    finally:
        db.close()  

def get_db_APIAdmin():
    db = SessionLocalAPIAdmin()
    try:    
        yield db
    finally:
        db.close()                    
        
def get_db_Users():
    db = SessionLocalUsers()
    try:    
        yield db
    finally:
        db.close()      

def get_db_UserAdmin():
    db = SessionLocalUsersAdmin()
    try:    
        yield db
    finally:
        db.close()      


