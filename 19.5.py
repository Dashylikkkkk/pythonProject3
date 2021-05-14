def prime(num):
    for i in range(num - 2):
        if num % (i + 2) == 0:
            return "Составное число"
    return "Простое число"
