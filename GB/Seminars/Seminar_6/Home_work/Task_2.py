# С помощью использования filter

# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

# Старый вариант решения задачи

# def find_num(num):
#     flag = False
#     for item in my_list:
#         if str(num) in item:
#             flag = True
#             break
#     return flag
#
#
# my_list = ['hjhjsdhj95sddf', 'sddsd', 'fdsfd', 'sdfdf', 'sdfdf']
# print(find_num(68))

# Решение задачи при помощи filter
def main():
    my_list = ['hjhjsdhj95sddf', 'sddsd', 'fdsfd', 98, 'sdfdf', 'sdfdf']
    find_num = 98
    new_list = list(filter(lambda x: str(find_num) in str(x), my_list))
    if len(new_list) > 0:
        print(f'Число {find_num} присутствует в списке в виде:', *new_list)
    else:
        print(f'Число {find_num} в списке {my_list} не найдено!')


if __name__ == '__main__':
    main()
