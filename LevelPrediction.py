from datetime import datetime, timedelta
import requests
import json


def floodPredict(data, timestamp):

    # Weather Variables
    json, adj1, adj2 = 0, 0, 0
    # Weather Forecast Data Retrieval Area
    url = "https://community-open-weather-map.p.rapidapi.com/forecast"
    querystring = {"lat": "27.18", "lon": "78"}
    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "472a861150mshddb699d3b264b0ap12a94cjsne7617bb16f8a"
    }
    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    x = response.json()
    if x["cod"] == "200":
        y = x["list"]
        json = 1
    # Adjustment of Result According to Rain

    def rainyDay():
        curr_dt = datetime.now()
        for j in range(0, 40):
            z = y[j]
            dt_obj = datetime.strptime(z["dt_txt"], "%Y-%m-%d %H:%M:%S")
            if(curr_dt+timedelta(seconds=rem1) < dt_obj):
                if("rain" in z):
                    a = z["rain"]
                    adj1 += a["3h"]
                    if(curr_dt+timedelta(seconds=rem2) < dt_obj):
                        adj2 += z["rain"]["3h"]
        rem1 -= int(0.1*adj1/m)
        rem2 -= int(0.1*adj2/m)

    # Converting Passed Objects ---> Arrays with key
    enumerate(data)
    enumerate(timestamp)

    h = 53  # Height of Dam in cm
    x, y, x2, n, xy, prev = 0, 0, 0, 0, 0, 0
    d0 = timestamp[0]  # Base Time ie of first Water Level Data
    case = False  # Control Variable for switching bw Rising and Falling Water Level

    for i in range(0, 50):
        level = data[i]
        # Switching b/w Rising and Falling
        if(prev > level ^ case):
            case = not case
            d0 = timestamp[i-1]
            x, y, x2, n, xy = 0, prev, 0, 1, 0
        prev = level
        # Manipulating variables used for calculation of reression
        n += 1
        d1 = timestamp[i]
        t = d1 - d0
        time = int(t.total_seconds())
        y += level
        x += time
        x2 += time*time
        xy += time*level

    d = n*x2 - x*x
    c = (y*x2 - x*xy)/d
    m = (n*xy - x*y)/d

    # Water Level Rising
    if(case == 0):
        # rem1 is the time after which water level will reach 100% FRL
        rem1 = int((h-c)/m - time)
        # rem2 is the time after which water level will reach 75% FRL
        rem2 = int((0.9*h-c)/m - time)
    # Water Level Falling
    else:
        # rem1 is the time after which water level will be half of current value
        rem1 = int((0.5*level-c)/m - time)
        # rem2 is the time after which water level will decrease by 10% of FRL
        rem2 = int((level-0.1*h-c)/m - time)

    rainyDay()  # Function Call for Rain Adjustments

    return(level, rem1, rem2, case)
