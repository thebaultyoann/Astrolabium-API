from sqlalchemy import create_engine,Column, Integer, Date, JSON, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../../files_user/')
from variable import DB_Username_API, DB_Password_API, DB_Username_Users, DB_Password_Users, DB_Container_Name, DB_Name_For_Api_Tables, DB_Name_For_Users_Tables


engineAPI = create_engine("mariadb+mariadbconnector://"+DB_Username_API+":"+DB_Password_API+"@"+DB_Container_Name+":3306/"+DB_Name_For_Api_Tables)
engineUsers = create_engine("mariadb+mariadbconnector://"+DB_Username_Users+":"+DB_Password_Users+"@"+DB_Container_Name+":3306/"+DB_Name_For_Users_Tables)

Base = declarative_base()
Base2 = declarative_base()
    
class DataDay(Base):
    __tablename__ = 'dataday'
    simulationDate = Column(Date, primary_key=True)
    sample = Column(Integer, primary_key=True)
    targetDays = Column(JSON)

class DataHour(Base):
    __tablename__ = 'datahour'
    simulationDate = Column(Date, primary_key=True)
    sample = Column(Integer, primary_key=True)
    targetHours = Column(JSON)

class Users(Base2):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(4),  unique=True, index=True)
    password_hashed = Column(String(60))
    activated = Column(Boolean, default=True)
    expiration_date = Column(Date)
    



SessionLocalAPI = sessionmaker(autocommit=False, autoflush=False, bind=engineAPI)
SessionLocalUsers = sessionmaker(autocommit=False, autoflush=False, bind=engineUsers)


#Dependency
def get_db_API():
    db = SessionLocalAPI()
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

     


