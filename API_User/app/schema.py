from pydantic import BaseModel, Field
from fastapi import Form
from datetime import date 
import numpy as np


#range of queries
sampleMin=1
sampleMax=100000

targetDayMin=1
targetDayMax=181

targetHourMin=1
targetHourMax=49


#Simulation
class DataDayBase(BaseModel):
    simulationDate: date

class DataDay(DataDayBase):
    sample : int = Field(..., example=1)
    targetDays : dict[str,float] = Field(..., example={str(i): float(np.random.random()*100) for i in range(1, 181)})

class DataHourBase(BaseModel):
    simulationDate: date

class DataHour(DataHourBase):
    sample : int = Field(..., example=1)
    targetHours : dict[str, float] = Field(..., example={str(i): float(np.random.random()*100) for i in range(1, 49)})

class DataDaySample(DataDayBase):
    sample : int = Field(..., ge=sampleMin, le=sampleMax, description=f"From {sampleMin} to {sampleMax}", example=1)

class DataHourSample(DataHourBase):
    sample : int = Field(..., ge=sampleMin, le=sampleMax, description=f"From {sampleMin} to {sampleMax}", example=1)

class DataDayTenThousandSample(DataDayBase):
    sampleStart : int = Field(..., ge=sampleMin, le=sampleMax-9999, description=f"From {sampleMin} to {sampleMax-9999}, give the 10000 following samples", example=1)

class DataDayThousandSample(DataDayBase):
    sampleStart : int = Field(..., ge=sampleMin, le=sampleMax-999, description=f"From {sampleMin} to {sampleMax-999}, give the 1000 following samples", example=1)

class DataDayHundredSample(DataDayBase):
    sampleStart : int = Field(..., ge=sampleMin, le=sampleMax-99, description=f"From {sampleMin} to {sampleMax-99}, give the 100 following samples", example=1)

class DataDayTargetedDay(DataDayBase):
    targetedDay : int = Field(..., ge=targetDayMin, le=targetDayMax, description="From 1 to 180", example=34)

class DataHourTargetedHour(DataHourBase):
    targetedHour : int = Field(..., ge=targetHourMin, le=targetHourMax, description="From 1 to 24", example=24)

class DataDayForTargetedDay(DataDayBase):
    sample : int = Field(..., example=1)
    targetDays : dict[str,float] = Field(..., example={'34':0})

class DataHourForTargetedHour(DataHourBase):
    sample : int = Field(..., example=1)
    targetHours: dict[str,float] = Field(..., example={'24':0})


#Authentifiation Class
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str

class UserPassword(User):
    password_hashed: str

class UserActivated(UserPassword):
    disabled: bool | None = None



