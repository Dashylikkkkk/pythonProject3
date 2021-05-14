letters = ('а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е')


def translate(text):
    global translated_text
    for i in text:
        if not i.lower() in letters:
            if len(translated_text) == 0:
                translated_text += i
            else:
                if not (translated_text[-1] == ' ' and i == ' '):
                    translated_text += i


translated_text = ''
translate(
    "Удивительный факт, но текст на языке НЕРАЗБОРЧИВО оказывается довольно просто читать. "
    "Достаточно небольшой тренировки - и вы сможете это делать.")
print(translated_text)
