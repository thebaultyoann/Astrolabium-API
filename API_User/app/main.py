from fastapi import Depends, FastAPI, Request
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Annotated
import app.schema as schema
import app.db as db
import app.authentification as authentification
import app.simulation as simulation
import asyncio
from functools import wraps

db.Base.metadata.create_all(bind=db.engineAPI)
db.Base2.metadata.create_all(bind=db.engineUsers)


queue = []
queue_numbers = 0
def handle_connexions(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        numero_queue = get_in_queue()
        while not check_queue(numero_queue):
            await asyncio.wait(1)
        return await func(*args, **kwargs)
    return wrapper

async def get_in_queue():
    global queue_numbers
    queue_numbers=(queue_numbers+1)%10000
    queue.append(queue_numbers)
    return queue_numbers

def check_queue(numero_queue):
    return queue[0]==numero_queue

def drop_from_queue():
    queue.pop(0)



#drop the first item
#when first or second, can get out of the wrapper to get working


app = FastAPI()


#Endpoints for data
@app.post("/simulationLongModel", response_model=list[schema.DataDay])
@handle_connexions
async def get_Simulation_For_Days(
    current_user: Annotated[schema.User, Depends(authentification.get_current_active_user)],
    payload: schema.DataDayBase,
    db: Session = Depends(db.get_db_API)
):
    data=simulation.getSimulationForDays(simulationDate=payload.simulationDate, db=db)
    drop_from_queue()
    return data

@app.post("/simulationShortModel", response_model=list[schema.DataHour])
async def get_Simulation_For_Hours(
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
