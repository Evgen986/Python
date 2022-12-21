# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random


def fractional_difference(new_list):
    minimal = 100
    maximal = 0
    for item_f in new_list:
        temp = (str(item_f).partition('.'))[2]
        if len(temp) == 1 and temp != '0':
            temp = temp + '0'
        if int(temp) < minimal:
            minimal = int(temp)
        if int(temp) > maximal:
            maximal = int(temp)
    return (maximal-minimal)/100


my_list = []
for item in range(random.randint(5, 10)+1):
    my_list.append(round(random.uniform(0.5, 10.5), 2))
print(f'{my_list} => {fractional_difference(my_list)}')
