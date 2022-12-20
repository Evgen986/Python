# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def sum_nums(num_f):  # Функция суммирования отдельных чисел
    symbol = num_f.find('.')
    if symbol > 0:  # Если число с плавающей точкой
        num_f = int(float(num_f) * 10 ** (len(num_f) - 1 - symbol))
        sum = 0
        while num_f:
            sum += num_f % 10
            num_f //= 10
    else:  # Иначе целочисленное значение
        num_f = int(num_f)
        sum = 0
        while num_f:
            sum += num_f % 10
            num_f //= 10
    return sum


flag = True
while flag:  # Проверка на корректность ввода через исключение
    num = input('Введите число: ')
    # Убираем '-' и заменяем ',' на точку '.',что бы исключить ошибку
    num = num.replace('-', '').replace(',', '.')
    try:
        float(num)
        flag = False
    except ValueError:
        print('Введено некорректное значение!')

print(f'{num} -> {sum_nums(num)}')
