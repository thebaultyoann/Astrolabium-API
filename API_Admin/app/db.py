from sqlalchemy import create_engine,Column, Integer, Date, JSON, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../../files/')
from variable import DB_Username_APIAdmin, DB_Password_APIAdmin, DB_Username_UserAdmin,DB_Password_UserAdmin,DB_Container_Name, DB_Name_For_Api_Tables, DB_Name_For_Users_Tables

engineAPIAdmin= create_engine("mariadb+mariadbconnector://"+DB_Username_APIAdmin+":"+DB_Password_APIAdmin+"@"+DB_Container_Name+":3306/"+DB_Name_For_Api_Tables)
engineUserAdmin = create_engine("mariadb+mariadbconnector://"+DB_Username_UserAdmin+":"+DB_Password_UserAdmin+"@"+DB_Container_Name+":3306/"+DB_Name_For_Users_Tables)

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

class UserAdmin(Base2):
    __tablename__ = 'useradmin'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(4),  unique=True, index=True)
    password_hashed = Column(String(60))
    twofa_key = Column(String(32))

SessionLocalAPIAdmin = sessionmaker(autocommit=False, autoflush=False, bind=engineAPIAdmin)
SessionLocalUsersAdmin = sessionmaker(autocommit=False, autoflush=False, bind=engineUserAdmin)


#Dependency
def get_db_APIAdmin():
    db = SessionLocalAPIAdmin()
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


