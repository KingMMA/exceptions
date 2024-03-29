"""
Ошибки (номера строк через пробел, данная строка - №2): 24-32!!!
"""


def f(x):
    """Вернуть значение функции.

    Функция не обрабатывает исключения.
    """
    return x**2 / (x + 2) - 3


k = int(input("Введите границу интервала [-k; k]: "))
h = float(input("Введите шаг табуляции: "))

x = -k
try:
    print("{:>10} {:>10}".format("x", "f(x)"))
    while x <= k:
        # Если во время вычисления функции возникнет ошибка,
        # при выводе необходимо указать прочерк "-"
        # Данный случай должен обрабатывать второй вложенный блок try
        try:
            print("{:10.2f} {:10.2f}".format(x, f(x)))
        except ZeroDivisionError:
            print("{:10.2f}\t{}".format(x, "  -"))
        x += h
    else:
        raise Exception
except Exception:
    print("Интервал должен быть позитивным числом!")

 
# --------------
# Пример вывода:
#
# Введите границу интервала [-k; k]: 5
# Введите шаг табуляции: 0.5
#          x       f(x)
#      -5.00     -11.33
#      -4.50     -11.10
#      -4.00     -11.00
#      -3.50     -11.17
#      -3.00     -12.00
#      -2.50     -15.50
#      -2.00          -
#      -1.50       1.50
#      -1.00      -2.00
#       ...
#       4.50       0.12
#       5.00       0.57