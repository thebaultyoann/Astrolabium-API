from sqlalchemy import Column, Integer, Date, JSON, String, Boolean
from app.db import Base

#Simulation
class DataDay(Base):
    __tablename__ = 'testwithdict'
    id = Column(Integer, primary_key=True)
    simulationDate = Column(Date)
    sample = Column(Integer)
    targetDays = Column(JSON)
