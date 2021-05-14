def defractalize(fractal):
    list = []
    for i in range(len(fractal)):
        if fractal[i] == fractal:
            list.append(i)
    for i in list:
        fractal.pop(i)


fractal = [2, 5]
fractal.append(fractal)
fractal.append(3)
fractal.append(fractal)
fractal.append(9)
defractalize(fractal)
print(fractal)
