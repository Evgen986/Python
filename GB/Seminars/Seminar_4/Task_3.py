# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

num_1 = int(input('Введите число : '))
num_2 = int(input('Введите число : '))
max_num = max(num_1, num_2)
min_num = min(num_1, num_2)
for i in range (max_num, num_1*num_2+1, max_num):
    if i % min_num == 0:
        NOK = i
        break
print(NOK)
