def palindrome(text):
    a = -1
    b = 0
    check = len(text) // 2
    while b != check:
        if text[b] == ' ':
            check += 1
            b += 1
        if text[a] == ' ':
            check -= 1
            a -= 1
        if text[b] != ' ' and text[a] != ' ':
            if text[b].upper() != text[a].upper():
                return "Не палиндром"
        a -= 1
        b += 1
    return "Палиндром"
