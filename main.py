import requests
import time
import json

from boltiot import Bolt
from GetSensorData import getSensorValue
from Database import InsertIntoTable, ExtractFromTable
from LevelPrediction import floodPredict
from datetime import timedelta

import conf

if __name__ == "__main__":

    H = 56

    while True:

        sensor_value = getSensorValue()

        if sensor_value == -999:
            print("Request was unsuccessful! Skipping")
            time.sleep(10)
            continue

        sensor_value = sensor_value.strip()

        if sensor_value == '':
            time.sleep(10)
            continue

        level = H - int(sensor_value)
        print("Water Level: ", level)

        InsertIntoTable(level,'SensorData')

        data, timestamp = ExtractFromTable('SensorData')

        if len(data) < 50:
            time.sleep(10)
            continue

        level, timeToFSL, timeTo75 = floodPredict(data, timestamp)
        InsertIntoTable(str(timedelta(seconds=timeToFSL)), 'RemTime')

        print("Current Level: ", level)
        print("Time to FSL: ", timedelta(seconds=timeToFSL))
        print("Time to 75%: ", timedelta(seconds=timeTo75))
        print("\n")

        time.sleep(10)