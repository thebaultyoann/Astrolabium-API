from pydantic import BaseModel, Json, Field
from fastapi import Form
from typing import Annotated
from datetime import date 

#range of queries
sampleMin=1
sampleMax=100000

targetDayMin=1
targetDayMax=180

#Simulation Class (client)
class DataDayBase(BaseModel):
    simulationDate: date

class DataDaySample(DataDayBase):
    sample : int = Field(..., ge=sampleMin, le=sampleMax, description="From 1 to 100000", example=1)

class DataDayTenThousandSample(DataDayBase):
    sampleStart : int = Field(..., ge=sampleMin, le=sampleMax-10000, description="From 1 to 90000, give the 10000 following samples", example=1)

class DataDayThousandSample(DataDayBase):
    sampleStart : int = Field(..., ge=sampleMin, le=sampleMax-1000, description="From 1 to 99000, give the 1000 following samples", example=1)

class DataDayHundredSample(DataDayBase):
    sampleStart : int = Field(..., ge=sampleMin, le=sampleMax-100, description="From 1 to 99900, give the 100 following samples", example=1)


class DataDayTargetedDay(DataDayBase):
    targetedDay : int = Field(..., ge=targetDayMin, le=targetDayMax, description="From 1 to 180", example=8)

class DataDay(DataDayBase):
    sample : int = Field(..., example=1)
    targetDays : dict[str,float] = Field(..., example={'1':0,'2':0,'3':0})
    class Config:
        from_attributes = True
        
class DataDayForTargetedDay(DataDayBase):
    sample : int = Field(..., example=1)
    targetDays : dict[str,float] = Field(..., example={'8':0})
    class Config:
        from_attributes = True

#Simulation Class (Admin)
class validationOnUpload(BaseModel):
    uploadSucess: bool      
    class Config:
        from_attributes = True

class DataDayInput(BaseModel):
        simulationDate: date
        sample: int
        targetDays : dict[str,float]

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

class TwoFaForm(BaseModel):
    two_fa_code: str = Form(..., regex=r"^\d{6}$")

class PasswordChangeForm(BaseModel):
    old_password_plain: Annotated[str, Form(..., description="Your old password")]
    new_password_plain: Annotated[str, Form(..., description="Your new password")]
    new_password_confirmation_plain: Annotated[str, Form(..., description="Confirm your new password")]






