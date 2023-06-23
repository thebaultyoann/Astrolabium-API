from fastapi import Depends, FastAPI, Body, Query
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Annotated
import app.modelsAPI as modelsAPI
import app.modelsUsers as modelsUsers
import app.schema as schema
import app.db as db
import app.authentification as authentification
import app.getsimulation as getsimulation

modelsAPI.Base.metadata.create_all(bind=db.engineAPI)
modelsUsers.Base.metadata.create_all(bind=db.engineUsers)

app = FastAPI()

#Endpoints for data
@app.post("/getSimulation", response_model=list[schema.DataDay])
def getSimulation(
    current_user: Annotated[schema.User, Depends(authentification.get_current_active_user)],
    payload: schema.DataDayBase,
    db: Session = Depends(db.get_db_API)
):
    return getsimulation.get_simulation(simulationDate=payload.simulationDate, db=db)

@app.post("/getSimulationSample", response_model=schema.DataDay)
def getSimulationSample(
    current_user: Annotated[schema.User, Depends(authentification.get_current_active_user)],
    payload : schema.DataDaySample,
    db:Session = Depends(db.get_db_API)
):
    return getsimulation.get_simulation_sample(simulationDate=payload.simulationDate,sample=payload.sample,db=db)

@app.post("/getSimulationForTargetDay", response_model=list[schema.DataDayForTargetedDay])
async def getSimulation(
    current_user: Annotated[schema.User,Depends(authentification.get_current_active_user)],
    payload: schema.DataDayTargetedDay,
    db:Session = Depends(db.get_db_API)
):
    return getsimulation.get_simulation_for_target_day(simulationDate=payload.simulationDate,targetedDay=payload.targetedDay,db=db)


#Endpoints for authentification
@app.post("/login", response_model=schema.Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db:Session = Depends(db.get_db_Users)
):
    return authentification.login_the_user_for_access_token(form_data=form_data,db=db)

@app.get("/user/me/", response_model=schema.User)
async def read_user_me(
    current_user: Annotated[schema.User, Depends(authentification.get_current_active_user)]
):
    return current_user

@app.post("/user/password/")
async def read_user_password(
    current_user: Annotated[schema.User, Depends(authentification.get_current_active_user)],
    password_form: schema.PasswordChangeForm = Depends(),
    db:Session=Depends(db.get_db_Users)
):
    return authentification.manage_password_changement(current_user=current_user,password_form=password_form,db=db)

