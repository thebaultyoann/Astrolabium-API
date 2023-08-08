from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Annotated
import app.schema as schema
import app.db as db
import app.authentification as authentification
import app.simulation as simulation

db.Base.metadata.create_all(bind=db.engineAPIAdmin)
db.Base2.metadata.create_all(bind=db.engineUserAdmin)

app = FastAPI()

#Endpoints for data
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

@app.post("/addSimulationSampleBySampleLongModel", response_model=schema.validationOnUpload)
def addSimulation(
    #current_admin_user: Annotated[schema.User, Depends(authentification.get_current_admin_user)],
    payload: schema.DataDayInput,
    db:Session = Depends(db.get_db_APIAdmin)
):
    return simulation.addSimulationSampleBySampleForDays(dict=payload, db=db)

@app.post("/addSimulationSampleBySampleShortModel", response_model=schema.validationOnUpload)
def addSimulation(
    #current_admin_user: Annotated[schema.User, Depends(authentification.get_current_admin_user)],
    payload: schema.DataHourInput,
    db:Session = Depends(db.get_db_APIAdmin)
):
    return simulation.addSimulationSampleBySampleForHours(dict=payload, db=db)

@app.post("/updateSimulationLongModel", response_model=schema.validationOnUpdate)
def update_Simulation_For_Days(
    #current_admin_user: Annotated[schema.User, Depends(authentification.get_current_admin_user)],
    payload: list[schema.DataDayInput],
    db:Session = Depends(db.get_db_APIAdmin)
):
    return simulation.updateSimulationForDays(dict=payload, db=db)

@app.post("/updateSimulationShortModel", response_model=schema.validationOnUpdate)
def update_Simulation_For_Hours(
    #current_admin_user: Annotated[schema.User, Depends(authentification.get_current_admin_user)],
    payload: list[schema.DataHourInput],
    db:Session = Depends(db.get_db_APIAdmin)
):
    return simulation.updateSimulationForHours(dict=payload, db=db)

@app.post("/updateSimulationBySampleLongModel", response_model=schema.validationOnUpdate)
def update_Simulation_By_Sample_For_Days(
    #current_admin_user: Annotated[schema.User, Depends(authentification.get_current_admin_user)],
    payload: schema.DataDayInput,
    db:Session = Depends(db.get_db_APIAdmin)
):
    return simulation.updateSimulationBySampleForDays(simulationDate=payload.simulationDate, sample=payload.sample, targetDays=payload.targetDays, db=db)

@app.post("/updateSimulationBySampleShortModel", response_model=schema.validationOnUpdate)
def update_Simulation_By_Sample_For_Hours(
    #current_admin_user: Annotated[schema.User, Depends(authentification.get_current_admin_user)],
    payload: schema.DataHourInput,
    db:Session = Depends(db.get_db_APIAdmin)
):
    return simulation.updateSimulationBySampleForHours(simulationDate=payload.simulationDate, sample=payload.sample, targetHours = payload.targetHours, db=db)

@app.post("/deleteSimulationLongModel", response_model=schema.validationOnDelete)
def update_Simulation_For_Days(
    current_admin_user: Annotated[schema.User, Depends(authentification.get_current_admin_user)],
    payload: schema.DataDayDeleteInput,
    db:Session = Depends(db.get_db_APIAdmin)
):
    return simulation.deleteSimulationForDays(dict=payload, db=db)

@app.post("/deleteSimulationShortModel", response_model=schema.validationOnDelete)
def update_Simulation_For_Hours(
    #current_admin_user: Annotated[schema.User, Depends(authentification.get_current_admin_user)],
    payload: schema.DataHourDeleteInput,
    db:Session = Depends(db.get_db_APIAdmin)
):
    return simulation.updateSimulationForHours(dict=payload, db=db)

#Endpoints for authentification
@app.post("/login", response_model=schema.Token)
async def login_for_admin_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    form_twofa: Annotated[schema.TwoFaForm, Depends()],
    db:Session = Depends(db.get_db_UserAdmin)
):
    return authentification.login_the_user_admin_for_access_token(form_data=form_data, form_twofa=form_twofa, db=db)
