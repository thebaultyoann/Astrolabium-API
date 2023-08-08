from sqlalchemy.orm import Session
import datetime
import app.db as database
import app.schema as schema

def add_simulation_for_days_on_db(db:Session, simulationDate: datetime.date, sample: float, targetDays: dict):
    new_simulation = database.DataDay(simulationDate=simulationDate, sample=sample, targetDays=targetDays)
    db.add(new_simulation)
    db.commit()
    return True

def add_simulation_for_hours_on_db(db:Session, simulationDate: datetime.date, sample: float, targetHours: dict):
    new_simulation = database.DataHour(simulationDate=simulationDate, sample=sample, targetHours=targetHours)
    db.add(new_simulation)
    db.commit()
    return True

def update_simulation_for_days_on_db(db:Session, simulationDate: datetime.date, sample: float, targetDays: dict):
    simulation = db.query(database.DataDay).filter((database.DataDay.simulationDate == simulationDate)&(database.DataDay.sample == sample)).first()
    simulation.simulationDate=simulationDate
    simulation.sample=sample
    simulation.targetDays=targetDays
    db.commit()
    return True

def update_simulation_for_hours_on_db(db:Session, simulationDate: datetime.date, sample: float, targetHours: dict):
    simulation = db.query(database.DataHour).filter((database.DataHour.simulationDate == simulationDate)&(database.DataHour.sample == sample)).first()
    simulation.simulationDate=simulationDate
    simulation.sample=sample
    simulation.targetHours=targetHours
    db.commit()
    return True

def delete_simulation_for_days_on_db(db:Session, simulationDate: datetime.date):
    simulation = db.query(database.DataDay).filter(database.DataDay.simulationDate == simulationDate).all()
    db.delete(simulation)
    db.commit()
    return True 

def delete_simulation_for_hours_on_db(db:Session, simulationDate: datetime.date):
    simulation = db.query(database.DataHour).filter(database.DataHour.simulationDate == simulationDate).all()
    db.delete(simulation)
    db.commit()
    return True 

def get_user_admin(db: Session, username: str):
    user_dict = db.query(database.UserAdmin).filter((database.UserAdmin.username == username)).first()
    return schema.UserTwoFA(
            id=user_dict.id,
            username=user_dict.username,
            password_hashed=user_dict.password_hashed,
            twofa_key=user_dict.twofa_key
            )