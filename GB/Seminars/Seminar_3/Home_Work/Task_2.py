# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import random


def product_mirror_pos(new_list):
    result_list = []
    if len(new_list) % 2 == 0:
        middle_list = len(new_list) // 2
    else:
        middle_list = len(new_list) // 2 + 1
    for index in range(middle_list):
        result_list.append(new_list[index]*new_list[-1-index])
    return result_list


my_list = []
for item in range(random.randint(5, 10)+1):
    my_list.append(random.randint(0, 10))
product_list = product_mirror_pos(my_list)
print(f'{my_list} => {product_mirror_pos(my_list)}')
