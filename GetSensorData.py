import requests
import time
import json
import conf
from boltiot import Bolt

mybolt = Bolt(conf.api_key,conf.device_id)
mybolt.serialBegin('9600')

def getSensorValue():
#Returns Sensor Value. Returns -999 if fails


	try:
		response = mybolt.serialRead("10")
		data = json.loads(response)

		if data["success"] != 1:
			print("Request not successful")
			print(response)
			return -999

		sensor_value = data["value"]
		return sensor_value

	except Exception as e:
		print("Something went wrong. Response from BOLT:")
		print(e)
		return -999
while True:

	sensor_value = getSensorValue()

	if sensor_value == -999:
		print("Request was unsuccessful! Skipping")
		continue

	print("Sensor Value: ",sensor_value)

	time.sleep(5)

