def catalan(n):
    answer = factorial(2 * n) / (factorial(n) * factorial(n + 1))
    return answer


def factorial(num):
    answer = 1
    while num != 0:
        answer *= num
        num -= 1
    return answer


for i in range(20):
    print(catalan(i))
