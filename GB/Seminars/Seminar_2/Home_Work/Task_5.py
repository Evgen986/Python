# Реализуйте алгоритм перемешивания списка.
import random


def get_list(num):  # Функция заполнения списка рандомными значениями
    my_list = []
    for i in range(num+1):
        my_list.append(random.randint(-50, 50))
    return my_list


def mix_list(int_list):  # Функция перемешивания списка
    new_mix_list = ['+' for i in range(len(int_list))]  # Создаем новый список заполненный '+', которые будут затираться по мере заполнения
    for i in range(len(int_list)):
        flag = True
        while flag:
            num_rand = random.randint(0, len(int_list)-1)  # Задаем рандомное число от 0 до длины списка перемешивания-1
            if new_mix_list[num_rand] == '+' and num_rand != i:  # Если в новом списке под индексом ранд. числа '+' и оно не равно i,
                flag = False                                     # то меняем флаг и выходим из цикла
        new_mix_list[num_rand] = int_list[i]  
    return new_mix_list


flag_w = True
while flag_w:
    n = input('Введите количество элементов списка: ')
    if n.isdigit():  # Проверка на корректность ввода
        n = int(n)
        flag_w = False
    else:
        print('Введено не корректное значение ! Попробуйте еще раз!')

my_list = get_list(n)
my_mix_list = mix_list(my_list)
print(f'Оригинальный лист: {my_list}')
print(f'Перемешанный лист: {my_mix_list}')
