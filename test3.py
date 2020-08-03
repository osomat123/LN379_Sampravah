import requests
import time
import json

from boltiot import Bolt
from GetSensorData import getSensorValue
from Database import InsertIntoTable, ExtractFromTable
from LevelPrediction import floodPredict
from datetime import timedelta
import conf


mybolt = Bolt(conf.api_key,conf.device_id)
mybolt.serialBegin('9600')

response = mybolt.serialRead("10")

url2 = "https://cloud.boltiot.com/remote/" + conf.api_key + "/serialRead?till=10&deviceName="+conf.device_id
url1 = "https://cloud.boltiot.com/remote/e29dab34-252a-4ef5-9270-73f269ee41da/serialBegin?baud=9600&deviceName=BOLT293673"

req1 = requests.get(url1)
req2 = requests.get(url2)
print(req1.text)
print(req2.text)
