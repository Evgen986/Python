# На вход программе подается строка текста, содержащая символы и число nn.
# Из данной строки формируется список. Напишите программу, которая разделяет список на вложенные подсписки так,
# что nn последовательных элементов принадлежат разным подспискам.
# my_list = []
# text = input()
# text = text.replace(' ', '')
# n = int(input())
# for i in range(n):
#     my_list.append([el for el in text[i::n]])
# print(my_list)


# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.
# matrix = [[el for el in input().split()] for _ in range(int(input()))]
# max_el = matrix[-1][-1]
# for row in range(len(matrix)):
#     for colons in range(len(matrix[row])):
#         if row >= len(matrix)-colons-1:
#             if matrix[row][colons] > max_el:
#                 max_el = matrix[row][colons]
# print(max_el)


# Напишите программу, которая транспонирует квадратную матрицу.
# matrix = [[el for el in input().split()] for _ in range(int(input()))]
# new_matrix = list()
# for row in range(len(matrix)):
#     temp = list()
#     for colons in range(len(matrix[row])):
#         temp.append(matrix[colons][row])
#     new_matrix.append(temp)
# for rows in new_matrix:
#     print(*rows)


# На вход программе подается нечетное натуральное число nn. Напишите программу, которая создает матрицу размером n
# n×n заполнив её символами '.'. Затем заполните символами * среднюю строку и столбец матрицы, главную и побочную
# диагональ матрицы. Выведите полученную матрицу на экран, разделяя элементы пробелами.
# n = int(input())
# matrix = [['.']*n for _ in range(n)]
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if i == j or j == len(matrix)-i-1 or i == len(matrix)//2 or j == len(matrix)//2:
#             matrix[i][j] = '*'
# for rows in matrix:
#     print(*rows)


# Напишите программу проверки симметричности квадратной матрицы относительно побочной диагонали.
# matrix = [[el for el in input().split()] for _ in range(int(input()))]
# new_matrix = list()
# for row in range(len(matrix)-1, -1, -1):
#     temp = list()
#     for colons in range(len(matrix[row])-1, -1, -1):
#         temp.append(matrix[colons][row])
#     new_matrix.append(temp)
# for i in range(len(matrix)):
#     for j in range(len(matrix)):
#         if matrix[i][j] != new_matrix[i][j]:
#             print('NO')
#             exit()
# else:
#     print('YES')


# Латинским квадратом порядка nn называется квадратная матрица размером n×n, каждая строка и каждый столбец
# которой содержат все числа от 1 до n. Напишите программу, которая проверяет,
# является ли заданная квадратная матрица латинским квадратом.
# n = int(input())
# matrix = [[el for el in input().split()] for _ in range(n)]
# for i in range(len(matrix)):
#     text = ''
#     for l in range(1, n+1):
#         text += str(l)
#     for j in range(len(matrix[i])):
#         text = text.replace(matrix[i][j], '')
#     if len(text) != 0:
#         print('NO')
#         exit()
#     for l in range(1, n+1):
#         text += str(l)
#     for j in range(len(matrix[i])):
#         text = text.replace(matrix[j][i], '')
#     if len(text) != 0:
#         print('NO')
#         exit()
# else:
#     print('YES')


# На шахматной доске 8×8 стоит ферзь. Отметьте положение ферзя на доске и все клетки,
# которые бьет ферзь. Клетку, где стоит ферзь, отметьте буквой Q, клетки, которые бьет ферзь, отметьте символами *,
# остальные клетки заполните точками.
# matrix = [['.' for el in range(8)] for rows in range(8)]
# coord = input()
# row = 8 - int(coord[1])
# col = (ord(coord[0]) - 97)
# print(col)
# for i in range(8):
#     for j in range(8):
#         if i == row:
#             matrix[i][j] = '*'
#         if j == col:
#             matrix[i][j] = '*'
#         if i == row + 1 or i == row - 1:
#             if j == col - 1 or j == col + 1:
#                 matrix[i][j] = '*'
#         if abs(row - i) == abs(col-j):
#                 matrix[i][j] = '*'
#
# matrix[row][col] = 'Q'
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end=' ')
#     print()


# На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n
# и заполняет её по следующему правилу:
# на главной диагонали на месте каждого элемента должно стоять число 0;
# на двух диагоналях, прилегающих к главной, число 1;
# на следующих двух диагоналях число 2, и т.д.
# n = int(input())
# matrix = [['.']*n for _ in range(n)]
# for i in range(len(matrix)):
#     counter = i
#     for j in range(len(matrix[i])):
#         matrix[i][j] = counter
#         if j < i:
#             counter -= 1
#         else:
#             counter += 1
# for row in matrix:
#     print(*row)