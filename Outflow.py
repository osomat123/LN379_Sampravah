from datetime import datetime, timedelta


def outflowfunc(inflow, water_level, timestamp):

    enumerate(inflow)
    enumerate(water_level)
    outflow = []
    height, area = 53, 960
    prev = 0
    x, y, x2, n, xy = 0, 0, 0, 0, 0
    d0 = timestamp[0]
    case = False

    for i in range(0, 49):
        diff = (water_level[i+1]-water_level[i])*area
        interval = timestamp[i+1]-timestamp[i]
        val = int(interval.total_seconds())
        wl = diff/val
        outflow[i] = wl - inflow[i]
        if(prev > outflow[i] ^ case):
            case = not case
            d0 = timestamp[i-1]
            x, y, x2, n, xy = 0, prev, 0, 1, 0
        prev = outflow[i]
        n += 1
        d1 = timestamp[i]
        t = d1 - d0
        time = int(t.total_seconds())
        y += outflow[i]
        x += time
        x2 += time*time
        xy += time*outflow[i]

    d = n*x2 - x*x
    c = (y*x2 - x*xy)/d
    rate = (n*xy - x*y)/d

    return (outflow, rate)
