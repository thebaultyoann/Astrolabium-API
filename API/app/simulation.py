from datetime import datetime, timedelta
import app.crud as crud

def get_simulation(simulationDate, db):
    data = crud.get_simulation_from_db(db=db, simulationDate=simulationDate)
    return data


def get_simulation_sample(simulationDate,sample,db):
    data = crud.get_sample_from_db(db=db, simulationDate=simulationDate, sample=sample)
    return data[0]

def get_simulation_for_target_day(simulationDate,targetedDay,db):
    data = crud.get_simulation_from_db(db=db, simulationDate=simulationDate)
    output = []
    for k in range(len(data)):
        simulationDateJSON = data[k].simulationDate
        sampleJson = data[k].sample
        targetDaysJson = data[k].targetDays[str(targetedDay)]
        output.append({
            'simulationDate':simulationDateJSON,
             'sample':sampleJson,
             'targetDays':{
                 str(targetedDay):targetDaysJson
                }
        })
    return output

def add_simulation(dict, db):
    for k in range(len(dict)):
        simulationDate = dict[k].simulationDate
        sample = dict[k].sample
        targetDays = dict[k].targetDays
        if not crud.add_simulation_on_db(db=db, simulationDate=simulationDate, sample=sample, targetDays=targetDays):
            return False
    return True


def add_simulation_one_by_one(dict, db):
    simulationDate = dict.simulationDate
    sample = dict.sample
    targetDays = dict.targetDays
    if not crud.add_simulation_on_db(db=db, simulationDate=simulationDate, sample=sample, targetDays=targetDays):
        return {"uploadSucess": False}
    return {"uploadSucess": True}