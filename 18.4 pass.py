a = input()
i = 0
for j in a:
    if '(' == j:
        i += 1
    elif ')' == j:
        i -= 1
    if i == -1:
        break
if i == 0:
    print('yes')
else:
    print('no')
