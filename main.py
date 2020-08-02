import requests
import time
import json

from boltiot import Bolt
from GetSensorData import getSensorValue
from Database import InsertIntoTable, ExtractFromTable
from LevelPrediction import floodPredict, weatherAPI
from Inflow_PoC import inflowfuncformodel
from datetime import timedelta

import conf

if __name__ == "__main__":

    H = 53
    t_api = 901
    t_db = 501

    while True:

        if t_api > 900:
            try:
                weather = weatherAPI()
            except Exception:
                time.sleep(10)
                continue
            t_api = 0

        sensor_value = getSensorValue()

        if sensor_value == -999:
            print("Request was unsuccessful! Skipping")
            t_api += 10
            t_db += 10
            time.sleep(10)
            continue

        sensor_value = sensor_value.strip()

        if sensor_value == '':
            t_api += 10
            t_db += 10
            time.sleep(10)
            continue

        level = H - int(sensor_value)
        print("Water Level: ", level)

        InsertIntoTable(level,'SensorData')

        data, timestamp = ExtractFromTable('SensorData')

        if len(data) < 50:
            time.sleep(10)
            time.sleep(10)
            continue

        level, timeToFSL, timeTo75 = floodPredict(data, timestamp)
        InsertIntoTable(str(timedelta(seconds=timeToFSL)), 'RemTime')

        inflow, slope = inflowfuncformodel(data, timestamp)

        InsertIntoTable(slope, 'InflowSlope')

        print("Current Level: ", level)
        print("Time to FSL: ", timedelta(seconds=timeToFSL))
        print("Time to 75%: ", timedelta(seconds=timeTo75))
        print("\n")

        if t_db>500:
            for val in range(len(inflow)):
                InsertIntoTable(inflow[val], 'Inflow', timestamp=str(timestamp[val]))
            t_db = 0

        time.sleep(10)
        t_api += 10
        t_db += 10
