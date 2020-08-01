import requests
import time
import math
import json

import conf
from boltiot import Bolt

def getSensorValue():
#Returns Sensor Value. Returns -999 if fails

	mybolt = Bolt(conf.api_key,conf.device_id)
	mybolt.serialBegin('9600')

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


