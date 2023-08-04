from fastapi import Depends, FastAPI, Body, Query
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Annotated
import app.schema as schema
import app.db as db
import app.authentification as authentification
import app.simulation as simulation

db.Base.metadata.create_all(bind=db.engineAPI)
db.Base.metadata.create_all(bind=db.engineAPIAdmin)
db.Base2.metadata.create_all(bind=db.engineUsers)
db.Base3.metadata.create_all(bind=db.engineUserAdmin)

app = FastAPI()

#Endpoints for data
@app.post("/simulationLongModel", response_model=list[schema.DataDay])
def get_Simulation_For_Days(
    current_user: Annotated[schema.User, Depends(authentification.get_current_active_user)],
    payload: schema.DataDayBase,
    db: Session = Depends(db.get_db_API)
):
    return simulation.getSimulationForDays(simulationDate=payload.simulationDate, db=db)

@app.post("/simulationShortModel", response_model=list[schema.DataHour])
def get_Simulation_For_Hours(
    current_user: Annotated[schema.User, Depends(authentification.get_current_active_user)],
    payload: schema.DataHourBase,
    db: Session = Depends(db.get_db_API)
):
    return simulation.getSimulationForHours(simulationDate=payload.simulationDate, db=db)

@app.post("/simulationSampleLongModel", response_model=schema.DataDay)
def get_Simulation_Sample_For_Days(
    current_user: Annotated[schema.User, Depends(authentification.get_current_active_user)],
    payload : schema.DataDaySample,
    db:Session = Depends(db.get_db_API)
):
    return simulation.getSimulationSampleForDays(simulationDate=payload.simulationDate,sample=payload.sample,db=db)

@app.post("/simulationSampleShortModel", response_model=schema.DataHour)
def get_Simulation_Sample_For_Hours(
    current_user: Annotated[schema.User, Depends(authentification.get_current_active_user)],
    payload : schema.DataHourSample,
    db:Session = Depends(db.get_db_API)
):
    return simulation.getSimulationSampleForHours(simulationDate=payload.simulationDate,sample=payload.sample,db=db)

@app.post("/simulationTenThousandSample", response_model=list[schema.DataDay])
def get_Simulation_Sample(
    current_user: Annotated[schema.User, Depends(authentification.get_current_active_user)],
    payload : schema.DataDayTenThousandSample,
    db:Session = Depends(db.get_db_API)
):
    return simulation.get_simulation_ten_thousand_sample(simulationDate=payload.simulationDate,sampleStart=payload.sampleStart,db=db)

@app.post("/simulationThousandSample", response_model=list[schema.DataDay])
def get_Simulation_Sample(
    current_user: Annotated[schema.User, Depends(authentification.get_current_active_user)],
    payload : schema.DataDayThousandSample,
    db:Session = Depends(db.get_db_API)
):
    return simulation.get_simulation_thousand_sample(simulationDate=payload.simulationDate,sampleStart=payload.sampleStart,db=db)

@app.post("/simulationHundredSample", response_model=list[schema.DataDay])
def get_Simulation_Sample(
    current_user: Annotated[schema.User, Depends(authentification.get_current_active_user)],
    payload : schema.DataDayHundredSample,
    db:Session = Depends(db.get_db_API)
):
    return simulation.get_simulation_hundred_sample(simulationDate=payload.simulationDate,sampleStart=payload.sampleStart,db=db)

@app.post("/simulationLongModelForTargetDay", response_model=list[schema.DataDayForTargetedDay])
async def get_Simulation_For_Target_Day(
    current_user: Annotated[schema.User,Depends(authentification.get_current_active_user)],
    payload: schema.DataDayTargetedDay,
    db:Session = Depends(db.get_db_API)
):
    return simulation.getSimulationForTargetDay(simulationDate=payload.simulationDate,targetedDay=payload.targetedDay,db=db)

@app.post("/simulationForTargetHour", response_model=list[schema.DataHourForTargetedHour])
async def get_Simulation_For_Target_Hour(
    current_user: Annotated[schema.User,Depends(authentification.get_current_active_user)],
    payload: schema.DataHourTargetedHour,
    db:Session = Depends(db.get_db_API)
):
    return simulation.getSimulationForTargetHour(simulationDate=payload.simulationDate,targetedHour=payload.targetedHour,db=db)


@app.post("/addSimulationLongModel", response_model=schema.validationOnUpload)
def add_Simulation_For_Days(
    #current_admin_user: Annotated[schema.User, Depends(authentification.get_current_admin_user)],
    payload: list[schema.DataDayInput],
    db:Session = Depends(db.get_db_APIAdmin)
):
    return simulation.addSimulationForDays(dict=payload, db=db)

@app.post("/addSimulationShortModel", response_model=schema.validationOnUpload)
def add_Simulation_For_Hours(
    #current_admin_user: Annotated[schema.User, Depends(authentification.get_current_admin_user)],
    payload: list[schema.DataHourInput],
    db:Session = Depends(db.get_db_APIAdmin)
):
    return simulation.addSimulationForHours(dict=payload, db=db)

@app.post("/addSimulationOneByOneLongModel", response_model=schema.validationOnUpload)
def addSimulation(
    #current_admin_user: Annotated[schema.User, Depends(authentification.get_current_admin_user)],
    payload: schema.DataDayInput,
    db:Session = Depends(db.get_db_APIAdmin)
):
    return simulation.addSimulationOneByOneForDays(dict=payload, db=db)

@app.post("/addSimulationOneByOneShortModel", response_model=schema.validationOnUpload)
def addSimulation(
    #current_admin_user: Annotated[schema.User, Depends(authentification.get_current_admin_user)],
    payload: schema.DataHourInput,
    db:Session = Depends(db.get_db_APIAdmin)
):
    return simulation.addSimulationOneByOneForHours(dict=payload, db=db)

#Endpoints for authentification
@app.post("/login", response_model=schema.Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db:Session = Depends(db.get_db_Users)
):
    return authentification.login_the_user_for_access_token(form_data=form_data,db=db)

@app.post("/login_admin", response_model=schema.Token)
async def login_for_admin_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    form_twofa: Annotated[schema.TwoFaForm, Depends()],
    db:Session = Depends(db.get_db_UserAdmin)
):
    return authentification.login_the_user_admin_for_access_token(form_data=form_data, form_twofa=form_twofa, db=db)

@app.get("/user/me/", response_model=schema.User)
async def read_user_me(
    current_user: Annotated[schema.User, Depends(authentification.get_current_active_user)]
):
    return current_user


# here some modifications needs to me made, first have a new user able to modify the data inside the dataday and datahours
# so we need routes to modify thoses with specific data specified
# we do we let the user modify its own password? the route already exists but means the user used by these get rights on modification on the table 
 
#adding a route following a isngle day 