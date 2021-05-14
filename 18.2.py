def password():
    a = []
    for i in range(3):
        p = input()
        a.append(p)
    if a[0] == 'password' or a[1] == 'password' or a[2] == 'password':
        print('Пароль принят')
    else:
        print('В доступе отказано')



