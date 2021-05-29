def encrypt_caesar(msg, shift=3):
    small = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    big = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    shift = shift % len(small)
    small_2 = small[shift:] + small[:shift]
    big_2 = big[shift:] + big[:shift]
    translation = msg.maketrans(small + big, small_2 + big_2)
    return msg.translate(translation)


def decrypt_caesar(msg, shift=3):
    return encrypt_caesar(msg, -1 * shift)
