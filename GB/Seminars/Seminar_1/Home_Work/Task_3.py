# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def correctness_check(coord):
    while True:
        try:
            num = int(input(f'Введите значение коордианты {coord}: '))
            if num == 0:
                print('Координата не может быть равна "0"')
            else:
                return num
        except ValueError:
            print('Введено не корректное значение, попробуйте еще раз!')

def plane_search(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4


coord_x = correctness_check('x')
coord_y = correctness_check('y')
print(
    f'Точка с координатами x={coord_x}, y={coord_y} находится в плоскости: {plane_search(coord_x, coord_y)}')
