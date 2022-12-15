# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

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


coord_1 = []
coord_2 = []
coord_1.append(correctness_check('x для точки №1'))
coord_1.append(correctness_check('y для точки №1'))
coord_2.append(correctness_check('x для точки №2'))
coord_2.append(correctness_check('y для точки №2'))
result = (((coord_2[0]-coord_1[0])**2)+((coord_2[1]-coord_1[1])**2))**0.5
# Не смог победить проблему расстояние между A (3,6); B (2,1) -> 5,09 - округляется до 5.10
print('Расстояние между точками = {:.2f}'.format(result))
