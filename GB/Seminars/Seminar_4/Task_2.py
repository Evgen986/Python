# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
#
# 1) с помощью математических формул нахождения корней квадратного уравнения
#
# 2) с помощью дополнительных библиотек Python

a = int(input('Введите значение a: '))
b = int(input('Введите значение b: '))
d = int(input('Введите значение d: '))

disc = b**2 - 4*a*d

if disc < 0:
    print()
elif disc == 1:
    x1 = b/(2*a)
else:
    x1 = (-b - disc**0.5)/(2*a)
    x2 = (-b + disc**0.5)/(2*a)

# Найти решение с помощью Sympy ОФОРМИТЬ С ПОМОЩЬЮ ФУНКЦИЙ