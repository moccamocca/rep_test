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


#б
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

# инверсия!

#е ж + з
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
print('ж-------------------------------------------------------------------------')
n = 5
str_my = ''
for i in range(n):
    for j in range(n):
        if (i >= j and j <= n - i - 1):
            str_my += '*'
        else:
            str_my += ' '

    str_my += '\n'

print(str_my)

#з к + а
print('з-------------------------------------------------------------------------')
n = 5
str_my = ''
for i in range(n):
    for j in range(n):
        if (i <= j and j >= n - i - 1):
            str_my += '*'
        else:
            str_my += ' '

    str_my += '\n'

print(str_my)



#и
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

