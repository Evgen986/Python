# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
#     Примеры:
    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

def get_numbers(num): 
    my_list = []
    my_max = None
    for i in range(num):
        my_list.append(int(input('Введите число: ')))
        if my_list[i] > my_max:
            my_max = my_list[i]
    return my_list, my_max

num_list, max_list = get_numbers(5)
print(list)
print(max_list)