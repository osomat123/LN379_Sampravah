from datetime import datetime, timedelta


def inflowfuncformodel(weir, timestamp):

    enumerate(weir)
    enumerate(timestamp)
    height, area = 53, 960
    h, q, time, prev = 0, 0, 0, 0
    x, y, x2, n, xy = 0, 0, 0, 0, 0
    m, c, d = 0, 0, 0
    case = False
    inflow = []
    d0 = timestamp[0]

    for i in range(0, 49):

        h = (weir[i+1]-weir[i])*area
        dur = timestamp[i+1]-timestamp[i]
        sec = int(dur.total_seconds())
        q = h/sec
        inflow.append(q)
        if (prev > q) ^ case:
            case = not case
            d0 = timestamp[i-1]
            x, y, x2, n, xy = 0, prev, 0, 1, 0
        prev = q
        n += 1
        d1 = timestamp[i]
        t = d1 - d0
        time = int(t.total_seconds())
        y += q
        x += time
        x2 += time*time
        xy += time*q

    d = n*x2 - x*x
    c = (y*x2 - x*xy)/d
    m = (n*xy - x*y)/d

    return (inflow, m)
