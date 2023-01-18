# С помощью использования **лямбд

# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
import time

# Старое решение

# def random_num():
#     second = time.time()
#     return int(second*9587) % 10
#
#
# num = random_num()
# print(num)

# Новое решение


def main():
    print((lambda x: int(x*9587) % 10)(time.time()))


if __name__ == '__main__':
    main()