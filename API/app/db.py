from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../../')
import variables

engineAPI = create_engine("mariadb+mariadbconnector://"+variables.DBUserForAPI+":"+variables.DBPasswordForAPI+"@"+variables.DBContainerName+":3306/"+variables.DBNameForAPI)
engineUsers = create_engine("mariadb+mariadbconnector://"+variables.DBUserForAPI+":"+variables.DBPasswordForAPI+"@"+variables.DBContainerName+":3306/"+variables.DBNameForUsers)
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
