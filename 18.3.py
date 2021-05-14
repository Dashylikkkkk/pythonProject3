def golden_radio(k):
    a = 1
    b = 1
    for i in range(k - 1):
        n = b
        b += a
        a = n
    print(b / a)


golden_radio(1)
golden_radio(2)
golden_radio(4)
