# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random


def sum_odd_positions (new_list):
    sum_pos = 0
    for index in range(1, len(new_list), 2):
        sum_pos += new_list[index]
    return sum_pos


my_list = []
for item in range(random.randint(5, 10)+1):
    my_list.append(random.randint(0, 15))
print(my_list)
print(f'Сумма нечетных позиций в списке = {sum_odd_positions(my_list)}')
