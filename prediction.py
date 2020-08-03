from datetime import datetime, timedelta


def floodPredict(data, timestamp):
    # Converting Passed Objects into Arrays with key
    enumerate(data)
    enumerate(timestamp)

    h = 53  # Height of Dam in cm
    x, y, x2, n, xy = 0, 0, 0, 0, 0
    d0 = timestamp[0]  # Base Time ie of first Water Level Data

    for i in range(0, 50):

        level = data[i]

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

    # rem1 is the time after which water level will reach 100% FRL
    rem1 = int((h-c)/m - time)
    # rem2 is the time after which water level will reach 75% FRL
    rem2 = int((0.75*h-c)/m - time)
    return(level, rem1, rem2)
