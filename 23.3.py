text = input().split()
letters = ["а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е"]
check = True
a = -1
for i in text:
    amount_of_vowels = len(list(filter(lambda x: x in letters, i)))
    if amount_of_vowels != a and a != -1:
        check = False
        break
    a = amount_of_vowels
if check:
    print("Парам пам-пам")
else:
    print("Пам парам")
