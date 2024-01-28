"""
Ошибки (номера строк через пробел, данная строка - №2): 11-15!!!
"""


def unemployment_rate(unemployed, employed):
   """Вернуть уровень безработицы (УБ) в долях 1.

      Расчет по формуле: УБ = Безработные / (Занятые + Безработные).
   """
   try:
      return unemployed / (unemployed + employed)
   except ZeroDivisionError:
      print("unemployed + employed in sum gives negative number")
      __import__("sys").exit()


unemployed = int(input("Введите кол-во безработных (чел.): "))
employed = int(input("Введите кол-во занятых (чел.): "))
rate = unemployment_rate(unemployed, employed)
print("Уровень безработицы = {:.1%}".format(rate))