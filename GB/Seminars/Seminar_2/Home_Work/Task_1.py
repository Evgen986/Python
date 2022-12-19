# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def sum_nums(num):  # Функция суммирования отдельных чисел
    symbol = num.find('.')
    if symbol > 0:    # Если число с плавающей точкой
        num = int(float(num)*10**(len(num)-1-symbol))
        sum = 0
        while num:
            sum += num % 10
            num //= 10
    else:   # Иначе целочисленное значение
        num = int(num)
        sum = 0
        while num:
            sum += num % 10
            num //= 10
    return sum


flag = True
while flag:     # Проверка на корректность ввода через исключение
    num = input('Введите число: ')
    # Убираем '-' и заменяем ',' на точку '.',что бы исключить ошибку
    num = num.replace('-', '').replace(',', '.')
    try:
        float(num)
        flag = False
    except ValueError:
        print('Введено некорректное значение!')

print(f'{num} -> {sum_nums(num)}')
