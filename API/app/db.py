from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('../../files/')
from variable import DB_Username_API, DB_Password_API, DB_Username_APIAdmin, DB_Password_APIAdmin, DB_Username_Users,DB_Password_Users,DB_Username_UserAdmin,DB_Password_UserAdmin,DB_Container_Name, DB_Name_For_Api_Tables, DB_Name_For_Users_Tables

engineAPI = create_engine("mariadb+mariadbconnector://"+DB_Username_API+":"+DB_Password_API+"@"+DB_Container_Name+":3306/"+DB_Name_For_Api_Tables)
engineAPIAdmin= create_engine("mariadb+mariadbconnector://"+DB_Username_APIAdmin+":"+DB_Password_APIAdmin+"@"+DB_Container_Name+":3306/"+DB_Name_For_Api_Tables)
engineUsers = create_engine("mariadb+mariadbconnector://"+DB_Username_Users+":"+DB_Password_Users+"@"+DB_Container_Name+":3306/"+DB_Name_For_Users_Tables)
engineUserAdmin = create_engine("mariadb+mariadbconnector://"+DB_Username_UserAdmin+":"+DB_Password_UserAdmin+"@"+DB_Container_Name+":3306/"+DB_Name_For_Users_Tables)
SessionLocalAPI = sessionmaker(autocommit=False, autoflush=False, bind=engineAPI)
SessionLocalAPIAdmin = sessionmaker(autocommit=False, autoflush=False, bind=engineAPI)
SessionLocalUsers = sessionmaker(autocommit=False, autoflush=False, bind=engineUsers)
SessionLocalUsersAdmin = sessionmaker(autocommit=False, autoflush=False, bind=engineUserAdmin)
Base = declarative_base()

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
    db = SessionLocalAPI()
    try:    
        yield db
    finally:
        db.close()      

def get_db_UserAdmin():
    db = SessionLocalAPI()
    try:    
        yield db
    finally:
        db.close()      


