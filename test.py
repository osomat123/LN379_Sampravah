import time

from Database import InsertIntoTable, ExtractFromTable
from LevelPrediction import floodPredict, weatherAPI
from datetime import timedelta
from Inflow_PoC import inflowfuncformodel


i = 0
j = 0
t_api = 901
t_db = 51

while True:

    print("Iteration: ", i)
    InsertIntoTable(i, 'SensorData')
    i += 0.05

    data, timestamp = ExtractFromTable('SensorData')

    if t_api >900:
        try:
            weather = weatherAPI()
        except Exception:
            time.sleep(1)
            continue
        t_api = 0

    if len(data)<50:
        time.sleep(1)
        t_api += 1
        t_db += 1
        continue


    level, rem1, rem2,case = floodPredict(data,timestamp,weather)
    InsertIntoTable(str(timedelta(seconds=rem1)), 'RemTime')

    inflow, slope = inflowfuncformodel(data,timestamp)

    InsertIntoTable(slope,'InflowSlope')


    print("Current Level: ",level)
    print("Time to FSL: ",timedelta(seconds=rem1))
    print("Time to 75%: ",timedelta(seconds=rem2))
    print("\n")

    if t_db >50:
        for val in range(len(inflow)):
            InsertIntoTable(inflow[val],'Inflow',timestamp=str(timestamp[val]))
        t_db = 0

    j += 1
    t_db+=1
    t_api += 1
    time.sleep(1)

