# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def product_numbers(num_f):
    product = []
    for i in range(1, num_f + 1):
        temp = 1
        for j in range(1, i + 1):
            temp *= j
        product.append(temp)
    return product


flag = True
while flag:
    num = input('Введите число N: ')
    if num.isdigit():
        num = int(num)
        flag = False
    else:
        print('Введено не корректное значение ! Попробуйте еще раз!')

print(f'{num} -> {product_numbers(num)}')
