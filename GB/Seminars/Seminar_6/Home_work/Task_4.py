# С помощью использования enumerate

# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

# Старое решение задачи
# def sum_odd_positions (new_list):
#     sum_pos = 0
#     for index in range(1, len(new_list), 2):
#         sum_pos += new_list[index]
#     return sum_pos
#
#
# my_list = []
# for item in range(random.randint(5, 10)+1):
#     my_list.append(random.randint(0, 15))
# print(my_list)
# print(f'Сумма нечетных позиций в списке = {sum_odd_positions(my_list)}')

# Новое решение задачи


def main():
    my_list = [random.randint(0, 15) for el in range(random.randint(5, 10))]
    sum_odd_positions = [el for i, el in enumerate(my_list, 1) if not i % 2]
    print(f'В списке {my_list} на нечетных позициях находятся {sum_odd_positions} их сумма = {sum(sum_odd_positions)}')


if __name__ == '__main__':
    main()