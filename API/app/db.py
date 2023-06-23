from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../../')
from variables import DBUserForAPI, DBPasswordForAPI, DBContainerName, DBNameForAPI, DBNameForUsers

engineAPI = create_engine("mariadb+mariadbconnector://"+DBUserForAPI+":"+DBPasswordForAPI+"@"+DBContainerName+":3306/"+DBNameForAPI)
engineUsers = create_engine("mariadb+mariadbconnector://"+DBUserForAPI+":"+DBPasswordForAPI+"@"+DBContainerName+":3306/"+DBNameForUsers)
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
