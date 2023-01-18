# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
#
# *Пример:*
#
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
from random import *

res = [randint(1, 10) for i in range(8)]
print('Задали список: ', res, '\n')

res_1 = list(filter(lambda x: res.count(x) == 1, res))
res_2 = [i for i in res if res.count(i) == 1]
res_3 = list(set(res))

print('Список уникальных элементов: ', res_1)
print('Список уникальных элементов: ', res_2)
print('Список уникальных элементов: ', res_3, '\n')
