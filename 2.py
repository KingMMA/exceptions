"""
Помилки (номери рядків через пробіл, цей рядок - №2): 14-16!!!
"""


def primes(a, b):
    """Повернути список простих чисел на відрізку від 'a' до 'b'."""
    res = []
    c = 0
    for i in range(a, b):
        for j in range(i):
            if i % (j + 1) == 0:
                c += 1
            if c > j:
                c = 0
                res.append(i)

    return res

print(primes(4, 10))