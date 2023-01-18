# С помощью использования zip

# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Старое решение

# import Task_4
#
#
# def read_file(name_file):  # Функция чтения из файла
#     with open(name_file, 'r') as file:
#         text = file.readline()
#     return text
#
#
# def sum_polynomials(poly_1, poly_2):  # Функция сложения многочленов
#     if len(poly_1) > len(poly_2):
#         polynomials_1 = str(poly_1).split()
#         polynomials_2 = str(poly_2).split()
#     else:
#         polynomials_1 = str(poly_2).split()
#         polynomials_2 = str(poly_1).split()
#     new_poly = ''
#     length_list = len(polynomials_1) - len(polynomials_2)
#     for index in range(0, length_list, 2):
#         new_poly += polynomials_1[index] + ' + '
#     for index in range(0, len(polynomials_2) - 2, 2):
#         index_1 = polynomials_1[index + length_list].find('x')
#         index_2 = polynomials_2[index].find('x')
#         if index_1 < 0 or index_2 < 0:
#             new_poly += str(int(polynomials_1[index + length_list]) + int(polynomials_2[index])) + ' = 0 '
#         else:
#             new_poly += str(int(polynomials_1[index + length_list][:index_1]) + int(polynomials_2[index][:index_2])) + \
#                         polynomials_1[index + length_list][index_1:] + ' + '
#     return new_poly
#
#
# def main():
#     Task_4.main()
#     p_1 = read_file('polynomial_1.txt')
#     p_2 = read_file('polynomial_2.txt')
#     print(f'многочлен №1 = {p_1}')
#     print(f'многочлен №2 = {p_2}')
#     print(f'сумма многочленов = {sum_polynomials(p_1, p_2)}')
#     Task_4.write_to_file('sum_polynomials.txt',
#                          f'сумма многочленов {p_1} и {p_2} \nравняется {sum_polynomials(p_1, p_2)}')
#
#
# if __name__ == '__main__':
#     main()

# Новое решение

# Для упрощения и т.к. в старом решении для созданий многочленов используется импорт из более ранней задачи, присвоил
# многочлены в строки

# Поставил себе задачу использовать zip() в данной задаче, но по моему еще больше ее усложнил(для чтения кода) :)

def sum_polynomials(poly_1: str, poly_2: str):  # Функция сложения многочленов
    poly_1 = poly_1.replace('+', ' + ').replace('x', ' x').split()
    poly_2 = poly_2.replace('+', ' + ').replace('x', ' x').split()
    result = [int(el_1) + int(el_2) if el_1.isdigit() and el_2.isdigit() else el_1\
              for el_1, el_2 in zip(poly_1[::-1], poly_2[::-1])]
    result.reverse()
    result = ''.join(map(str, result))
    if len(poly_1) != len(poly_2):
        symbol = result[result.find('x'):result.find('x') + 3]
        if len(poly_1) > len(poly_2):
            result = ''.join(map(str, poly_1[:poly_1.index(symbol)+1])) + '+' + result + '=0'
        else:
            result = ''.join(map(str, poly_2[:poly_1.index(symbol)+1]))+ '+' + result + '=0'
    return result


def main():
    p_1 = '35x^5+42x^4+12x^3+3x^2+46x+5'
    p_2 = '12x^6+14x^5+24x^4+21x^3+9x^2+64x+25'
    print(f'Многочлен №1 = {p_1}')
    print(f'Многочлен №2 = {p_2}')
    print(f'сумма многочленов = {sum_polynomials(p_1, p_2)}')


if __name__ == '__main__':
    main()
