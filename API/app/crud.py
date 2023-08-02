from sqlalchemy.orm import Session
import datetime
import app.db as database
import app.schema as schema

def get_simulation_from_db(db: Session, simulationDate: datetime.date):
    return db.query(database.DataDay).filter(database.DataDay.simulationDate == simulationDate).all()

def get_sample_from_db(db: Session, simulationDate: datetime.date, sample: float):
    return db.query(database.DataDay).filter((database.DataDay.simulationDate == simulationDate)&(database.DataDay.sample == sample)).all()

def add_simulation_on_db(db:Session, simulationDate: datetime.date, sample: float, targetDays: dict):
    new_simulation = database.DataDay(simulationDate=simulationDate, sample=sample, targetDays=targetDays)
    db.add(new_simulation)
    db.commit()
    return True


def get_user(db: Session, username: str):
    user_dict = db.query(database.Users).filter((database.Users.username == username)).first()
    return schema.UserActivated(
        id=user_dict.id,
        username=user_dict.username,
        password_hashed=user_dict.password_hashed,
        disabled=user_dict.disabled
    )

def get_user_admin(db: Session, username: str):
    user_dict = db.query(database.UserAdmin).filter((database.UserAdmin.username == username)).first()
    return schema.UserPassword(
        id=user_dict.id,
        username=user_dict.username,
        password_hashed=user_dict.password_hashed
    )

def change_user_password(db: Session, username:str, new_password_hashed:str):
    user = db.query(database.Users).filter((database.Users.username == username)).first()
    user.password_hashed = new_password_hashed
    db.commit()
    db.refresh(user)
    return True

def get_admin(db):
    return db.query(database.UserAdmin).first()
