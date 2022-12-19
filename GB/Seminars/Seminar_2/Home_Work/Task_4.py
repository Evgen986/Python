# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

def get_list(num):
    my_list = []
    for i in range(-num, num+1):
        my_list.append(i)
    return my_list

flag = True
while flag:
    n = input('Введите число N>2: ')
    if n.isdigit() and int(n)>2:
        n = int(n)
        flag = False
    else:
        print('Введено не корректное значение ! Попробуйте еще раз!')

my_list = get_list(n)
print(my_list)

file = open('file.txt', 'r')
first_index = int(file.readline())
second_index = int(file.readline())
third_index = int(file.readline())
four_index = int(file.readline())
product_1 = my_list[first_index]*my_list[second_index]
product_2 = my_list[third_index]*my_list[four_index]
print(f'first_index - {first_index}, second_index - {second_index}, third_index - {third_index}, four_index - {four_index}')
print(f'product_1 - {product_1}')
print(f'product_2 - {product_2}')