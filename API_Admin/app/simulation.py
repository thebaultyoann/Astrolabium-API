import app.crud as crud

def addSimulationForDays(dict, db):
    for k in range(len(dict)):
        simulationDate = dict[k].simulationDate
        sample = dict[k].sample
        targetDays = dict[k].targetDays
        if not crud.add_simulation_for_days_on_db(db=db, simulationDate=simulationDate, sample=sample, targetDays=targetDays):
            return {"uploadSucess": False}
    return {"uploadSucess": True}

def addSimulationForHours(dict, db):
    for k in range(len(dict)):
        simulationDate = dict[k].simulationDate
        sample = dict[k].sample
        targetHours = dict[k].targetHours
        if not crud.add_simulation_for_hours_on_db(db=db, simulationDate=simulationDate, sample=sample, targetHours=targetHours):
            return {"uploadSucess": False}
    return {"uploadSucess": True}

def addSimulationOneByOneForDays(dict, db):
    simulationDate = dict.simulationDate
    sample = dict.sample
    targetDays = dict.targetDays
    if not crud.add_simulation_for_days_on_db(db=db, simulationDate=simulationDate, sample=sample, targetDays=targetDays):
        return {"uploadSucess": False}
    return {"uploadSucess": True}

def addSimulationOneByOneForHours(dict, db):
    simulationDate = dict.simulationDate
    sample = dict.sample
    targetHours = dict.targetHours
    if not crud.add_simulation_for_hours_on_db(db=db, simulationDate=simulationDate, sample=sample, targetHours=targetHours):
        return {"uploadSucess": False}
    return {"uploadSucess": True}