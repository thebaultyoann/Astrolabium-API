from sqlalchemy.orm import Session
import datetime
import app.db as database
import app.schema as schema

def get_simulation_for_days_from_db(db: Session, simulationDate: datetime.date):
    return db.query(database.DataDay).filter(database.DataDay.simulationDate == simulationDate).all()

def get_simulation_for_hours_from_db(db: Session, simulationDate: datetime.date):
    return db.query(database.DataHour).filter(database.DataHour.simulationDate == simulationDate).all()

def get_sample_for_days_from_db(db: Session, simulationDate: datetime.date, sample: float):
    return db.query(database.DataDay).filter((database.DataDay.simulationDate == simulationDate)&(database.DataDay.sample == sample)).first()

def get_sample_for_hours_from_db(db: Session, simulationDate: datetime.date, sample: float):
    return db.query(database.DataHour).filter((database.DataHour.simulationDate == simulationDate)&(database.DataHour.sample == sample)).first()

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
    return schema.UserTwoFA(
            id=user_dict.id,
            username=user_dict.username,
            password_hashed=user_dict.password_hashed,
            twofa_key=user_dict.twofa_key
        )

def change_user_password(db: Session, username:str, new_password_hashed:str):
    user = db.query(database.Users).filter((database.Users.username == username)).first()
    user.password_hashed = new_password_hashed
    db.commit()
    db.refresh(user)
    return True

def get_admin(db):
    return db.query(database.UserAdmin).first()
