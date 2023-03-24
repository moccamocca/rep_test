# dz
#1
try:
    x1 = input("Введите число 1: ")
    x2 = input("Введите число 2: ")
    x3 = input("Введите число 3: ")

    res = int(x1 + x2 + x3)
    print("Итоговое число = ", res)
except ValueError:
    print("Ошибка приведения типов.")

#2
try:
    x1 = int(input("Введите четырехзначное число: "))
    razr1 = x1 // 1000
    razr2 = (x1 % 1000) // 100
    razr3 = ((x1 % 1000) % 100) // 10
    razr4 = ((x1 % 1000) % 100) % 10

    res = razr1 * razr2 * razr3 * razr4
    print(razr1, razr2, razr3, razr4, sep=" * ", end=" = ")
    print(res)
except ValueError:
    print("Ошибка приведения типов.")

#3
try:
    x = int(input("Введите количество метров: "))

    x_sm = x * 100
    x_dm = x * 10
    x_mm = x * 1000
    x_mil = x * 0.00062

    print(x, "м = \n", x_sm, "см\n", x_dm, "дм\n", x_mm, "мм\n", x_mil, "миль")
except ValueError:
    print("Ошибка приведения типов.")

#4
try:
    x1 = int(input("Введите размер основания: "))
    x2 = int(input("Введите размер высоты: "))

    s = 0.5 * x1 * x2

    print("Площадь треугольника = ", s)
except ValueError:
    print("Ошибка приведения типов.")

#5
try:
    x = int(input("Введите четырехзначное число: "))
    razr1 = str(x // 1000)
    razr2 = str((x % 1000) // 100)
    razr3 = str(((x % 1000) % 100) // 10)
    razr4 = str(((x % 1000) % 100) % 10)

    res = razr4 + razr3 + razr2 + razr1  # 1230 не переводить в int чтобы не потерять 0  вначале

    print(x, " = ", res)
except ValueError:
    print("Ошибка приведения типов.")


