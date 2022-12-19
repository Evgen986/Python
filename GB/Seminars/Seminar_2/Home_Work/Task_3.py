# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def set_sequence(num_f):
    my_dict = []
    for i in range(1, num_f + 1):
        my_dict.append(round((1 + 1 / i) ** i))
    return my_dict


flag = True
while flag:
    num = input('Введите число N: ')
    if num.isdigit():
        num = int(num)
        flag = False
    else:
        print('Введено не корректное значение ! Попробуйте еще раз!')
print(f'{num} -> {set_sequence(num)}')
