def sum_gema(word):
    sum = 0
    for i in word:
        i = i.upper()
        sum += ord(i) - ord('A') + 1
    return sum


print("Для остановки ввода введите пустую строку")
words = []
temp = ' '
while True:
    temp = input()
    if temp == '':
        break
    words.append((temp, sum_gema(temp)))
words.sort()
for i in words:
    print(i[0])
