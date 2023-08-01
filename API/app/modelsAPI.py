from sqlalchemy import Column, Integer, Date, JSON
from app.db import Base

#Simulation
class DataDay(Base):
    __tablename__ = 'dataday'
    id = Column(Integer, primary_key=True)
    simulationDate = Column(Date)
    sample = Column(Integer)
    targetDays = Column(JSON)
