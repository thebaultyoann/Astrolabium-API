import app.crud as crud

def getSimulationForDays(simulationDate, db):
    return crud.get_simulation_for_days_from_db(db=db, simulationDate=simulationDate)

def getSimulationForDays2(simulationDate, db):
    returned_data=[]
    for sample in range(1, 100000):
        returned_data.append(crud.get_sample_for_days_from_db(db=db, simulationDate=simulationDate, sample=sample))
    return returned_data


def getSimulationForHours(simulationDate, db):
    data = crud.get_simulation_for_hours_from_db(db=db, simulationDate=simulationDate)
    return data

def getSimulationSampleForDays(simulationDate,sample,db):
    return crud.get_sample_for_days_from_db(db=db, simulationDate=simulationDate, sample=sample)

def getSimulationSampleForHours(simulationDate,sample,db):
    return crud.get_sample_for_hours_from_db(db=db, simulationDate=simulationDate, sample=sample)


def get_simulation_ten_thousand_sample(simulationDate,sampleStart,db):
    returned_data=[]
    for sample in range(sampleStart, sampleStart+9999):
        returned_data.append(crud.get_sample_for_days_from_db(db=db, simulationDate=simulationDate, sample=sample))
    return returned_data

def get_simulation_thousand_sample(simulationDate,sampleStart,db):
    returned_data=[]
    for sample in range(sampleStart, sampleStart+999):
        returned_data.append(crud.get_sample_for_days_from_db(db=db, simulationDate=simulationDate, sample=sample))
    return returned_data

def get_simulation_hundred_sample(simulationDate,sampleStart,db):
    returned_data=[]
    for sample in range(sampleStart, sampleStart+99):
        returned_data.append(crud.get_sample_for_days_from_db(db=db, simulationDate=simulationDate, sample=sample))
    return returned_data


def getSimulationForTargetDay(simulationDate,targetedDay,db):
    data = crud.get_simulation_for_days_from_db(db=db, simulationDate=simulationDate)
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

def getSimulationForTargetHour(simulationDate,targetedHour,db):
    data = crud.get_simulation_for_hours_from_db(db=db, simulationDate=simulationDate)
    output = []
    for k in range(len(data)):
        simulationDateJSON = data[k].simulationDate
        sampleJson = data[k].sample
        targetHoursJson = data[k].targetHours[str(targetedHour)]
        output.append({
            'simulationDate':simulationDateJSON,
             'sample':sampleJson,
             'targetDays':{
                 str(targetedHour):targetHoursJson
                }
        })
    return output
