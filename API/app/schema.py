from pydantic import BaseModel, Json, Field
from fastapi import Form
from typing import Annotated
from datetime import date 
import numpy as np


#range of queries
sampleMin=1
sampleMax=100000

targetDayMin=1
targetDayMax=180

targetHourMin=1
targetHourMax=24


#Simulation
class DataDayBase(BaseModel):
    simulationDate: date

class DataDay(DataDayBase):
    sample : int = Field(..., example=1)
    targetDays : dict[str,float] = Field(..., example={str(i): float(np.random.random()*100) for i in range(1, 180)})

class DataHourBase(BaseModel):
    simulationDate: date

class DataHour(DataHourBase):
    sample : int = Field(..., example=1)
    targetHours : dict[str, float] = Field(..., example={str(i): float(np.random.random()*100) for i in range(1, 24)})

class DataDaySample(DataDayBase):
    sample : int = Field(..., ge=sampleMin, le=sampleMax, description=f"From {sampleMin} to {sampleMax}", example=1)

class DataHourSample(DataHourBase):
    sample : int = Field(..., ge=sampleMin, le=sampleMax, description=f"From {sampleMin} to {sampleMax}", example=1)

class DataDayTenThousandSample(DataDayBase):
    sampleStart : int = Field(..., ge=sampleMin, le=sampleMax-10000, description=f"From {sampleMin} to {sampleMax-10000}, give the 10000 following samples", example=1)

class DataDayThousandSample(DataDayBase):
    sampleStart : int = Field(..., ge=sampleMin, le=sampleMax-1000, description=f"From {sampleMin} to {sampleMax-1000}, give the 1000 following samples", example=1)

class DataDayHundredSample(DataDayBase):
    sampleStart : int = Field(..., ge=sampleMin, le=sampleMax-100, description=f"From {sampleMin} to {sampleMax-100}, give the 100 following samples", example=1)

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


#Simulation Class (Admin)
class validationOnUpload(BaseModel):
    uploadSucess: bool      

class DataDayInput(BaseModel):
        simulationDate: date
        sample: int
        targetDays : dict[str,float]

class DataHourInput(BaseModel):
        simulationDate: date
        sample: int
        targetHours : dict[str,float]


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

class UserTwoFA(UserPassword):
    twofa_key: str

class UserActivated(UserPassword):
    disabled: bool | None = None

class TwoFaForm(BaseModel):
    twofa_code: str = Form(..., regex=r"^\d{6}$")   




