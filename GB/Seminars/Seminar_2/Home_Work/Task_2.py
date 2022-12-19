# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def product_numbers(num):
    product = []
    for i in range(1, num+1):
        temp = 1
        for j in range(1, i+1):
            temp *= j        
        product.append(temp)
    return product

flag = True
while flag:
    n = input('Введите число N: ')
    if n.isdigit():
        n = int(n)
        flag = False
    else:
        print('Введено не корректное значение ! Попробуйте еще раз!')

print(f'{n} -> {product_numbers(n)}')