n = input("Введите буквенное обозначение рисунка для отображения: ")

# а
if n.lower() == 'а':
    print('A-------------------------------------------------------------------------')
    str_my = ''
    for i in range(5):
        for j in range(5):
            if i <= j:
                str_my += '*'
            else:
                str_my += ' '

        str_my += '\n'

    print(str_my)


# б
elif n.lower() == 'б':
    print('б-------------------------------------------------------------------------')
    str_my = ''
    for i in range(5):
        for j in range(5):
            if i >= j:
                str_my += '*'
            else:
                str_my += ' '

        str_my += '\n'

    print(str_my)


#в
elif n.lower() == 'в':
    print('в-------------------------------------------------------------------------')
    n = 5
    str_my = ''
    for i in range(n):
        for j in range(n):
            if (j < n - i) and (i <= j):
                str_my += '*'
            else:
                str_my += ' '

        str_my += '\n'

    print(str_my)

#г
elif n.lower() == 'г':
    print('г-------------------------------------------------------------------------')
    n = 5
    str_my = ''
    for i in range(n):
        for j in range(n):
            if (i >= j) and (j >= n - i - 1):
                str_my += '*'
            else:
                str_my += ' '

        str_my += '\n'

    print(str_my)

#д
elif n.lower() == 'д':
    print('д-------------------------------------------------------------------------')
    n = 5
    str_my = ''
    for i in range(n):
        for j in range(n):
            if ((j < n - i) and (i <= j)) or ((i >= j) and (j >= n - i - 1)):
                str_my += '*'
            else:
                str_my += ' '

        str_my += '\n'

    print(str_my)

#е = ж + з
elif n.lower() == 'е':
    print('е-------------------------------------------------------------------------')
    n = 5
    str_my = ''
    for i in range(n):
        for j in range(n):
            if (i >= j and j <= n - i - 1) or (i <= j and j >= n - i - 1):
                str_my += '*'
            else:
                str_my += ' '

        str_my += '\n'

    print(str_my)

#ж
elif n.lower() == 'ж':
    print('ж-------------------------------------------------------------------------')
    n = 5
    str_my = ''
    for i in range(n):
        for j in range(n):
            if (i >= j) and (j <= n - i - 1):
                str_my += '*'
            else:
                str_my += ' '

        str_my += '\n'

    print(str_my)

#з к + а
elif n.lower() == 'з':
    print('з-------------------------------------------------------------------------')
    n = 5
    str_my = ''
    for i in range(n):
        for j in range(n):
            if (i <= j) and (j >= n - i - 1):
                str_my += '*'
            else:
                str_my += ' '

        str_my += '\n'

    print(str_my)

#и
elif n.lower() == 'и':
    print('и-------------------------------------------------------------------------')
    n = 5
    str_my = ''
    for i in range(n):
        for j in range(n):
            if j <= n - i - 1:
                str_my += '*'
            else:
                str_my += ' '

        str_my += '\n'

    print(str_my)

#k
elif n.lower() == 'к':
    print('к-------------------------------------------------------------------------')
    n = 5
    str_my = ''
    for i in range(n):
        for j in range(n):
            if j >= n - i - 1:
                str_my += '*'
            else:
                str_my += ' '

        str_my += '\n'

    print(str_my)
else:
    print("Введено неверное значение.")


