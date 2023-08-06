from pydantic import BaseModel
from fastapi import Form
from datetime import date 

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

class TwoFaForm(BaseModel):
    twofa_code: str = Form(..., regex=r"^\d{6}$")   




