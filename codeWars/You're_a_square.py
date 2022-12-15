# Учитывая целое число, определите, является ли это квадратным числом
def is_square(n):
    return n == (n**0.5)*(n**0.5) 

num = 25
print(is_square(num))