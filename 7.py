"""
Ошибки (номера строк через пробел, данная строка - №2): 8-11 !!!
"""


def power(x, y=2):
    """Вернуть x^y."""
    if y < 0:
        return 1/x * power(x, abs(y) - 1)
    elif int(y) != y:
        return x**y
    elif y == 0:
        return 1
    else:
        return x * power(x, y - 1)


x = float(input("x="))
y = float(input("y="))
print(power(x, y))