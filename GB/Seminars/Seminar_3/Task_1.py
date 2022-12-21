# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
import time


def random_num():
    second = time.time()
    return int(second*9587) % 10


num = random_num()
print(num)
