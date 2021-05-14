def fractal_print(obj):
    fractalId = 0
    for i in range(len(obj)):
        if obj[i] == obj:
            fractalId = i
    fractalForPrint = obj[:]
    fractalForPrint[fractalId] = obj
    print(fractalForPrint)


fractal = [3]
fractal.append(fractal)
fractal.append(2)
fractal_print(fractal)

fractal = [3]
fractal.append(fractal)
fractal_print(fractal)
