import serial

def sensorValue(arduino):

    data = arduino.readline()

    val = data.decode('utf-8')

    try:
        data = int(val.strip())

    except Exception:
        return -999

    return val