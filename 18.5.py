def equation(a, b):
    x1 = float(a.split(';')[0])
    y1 = float(a.split(';')[1])
    x2 = float(b.split(';')[0])
    y2 = float(b.split(';')[1])
    b = (x2 * y1) - (x1 * y2)
    if y2 - y1 == 0:
        print(round((b / (x2 - x1)), 10))
    elif x2 - x1 == 0:
        print(round((b / (y2 - y1)), 10))
    else:
        k = (y2 - y1) / (x2 - x1)
        b /= x2 - x1
        print(round(k, 10), round(b, 10))


equation("4;6.9", "-5.2;6.9")
equation("0;0", "0;4")
equation("0;0", "1;1")
