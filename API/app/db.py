from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../../files/')
from variable import DB_Username_For_API, DB_Password_For_API, DB_Container_Name, DB_Name_For_API, DB_Name_For_Users

engineAPI = create_engine("mariadb+mariadbconnector://"+DB_Username_For_API+":"+DB_Password_For_API+"@"+DB_Container_Name+":3306/"+DB_Name_For_API)
engineUsers = create_engine("mariadb+mariadbconnector://"+DB_Username_For_API+":"+DB_Password_For_API+"@"+DB_Container_Name+":3306/"+DB_Name_For_Users)
SessionLocalAPI = sessionmaker(autocommit=False, autoflush=False, bind=engineAPI)
SessionLocalUsers = sessionmaker(autocommit=False, autoflush=False, bind=engineUsers)
Base = declarative_base()

#Dependency
def get_db_API():
    db = SessionLocalAPI()
    try:    
        yield db
    finally:
        db.close()                  
        
def get_db_Users():
    db = SessionLocalAPI()
    try:    
        yield db
    finally:
        db.close()      
