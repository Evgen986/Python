# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81

import os
import random

def main():
    os.system('cls')
    num = int(input('Введите число N: '))
    for i in range(num):
        print(random.randint(-100, 100), end=', ')

main()
