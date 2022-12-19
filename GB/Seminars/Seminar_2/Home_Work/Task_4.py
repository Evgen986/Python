# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

def get_list(num):  # Функция заполнения списка
    my_list = []
    for i in range(-num, num+1):
        my_list.append(i)
    return my_list

flag = True  # Ввод числа N от пользователя и проверка на корректность
while flag:
    n = input('Введите число N>2: ')
    if n.isdigit() and int(n)>2:
        n = int(n)
        flag = False
    else:
        print('Введено не корректное значение ! Попробуйте еще раз!')

my_list = get_list(n)
print(my_list)

# Работа с файлом проверка с исключением (открытие, присваивание переменным значений хранящихся в файле, закрытие файла)
try:
    file = open('file.txt', 'r')
    first_index = int(file.readline())
    second_index = int(file.readline())
    third_index = int(file.readline())
    four_index = int(file.readline())
    file.close()
except FileNotFoundError:
    print('Файл не найден!')
    exit()  # В случае обнаружения исключения прерываем выполнение программы

# Перемножение данных хранящихся в листе согласно полученным индексам
product_1 = my_list[first_index]*my_list[second_index]
product_2 = my_list[third_index]*my_list[four_index]

print(f'first_index - {first_index}, second_index - {second_index}, third_index - {third_index}, four_index - {four_index}')
print(f'{my_list[first_index]}*{my_list[second_index]} = {product_1}')
print(f'{my_list[third_index]}*{my_list[four_index]} = {product_2}')