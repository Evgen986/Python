len_m1 = [int(el) for el in input().split()]
matrix1 = list()
for _ in range(len_m1[0]):
    matrix1.append([int(el) for el in input().split()])

input()

len_m2 = [int(el) for el in input().split()]
matrix2 = list()
for _ in range(len_m2[0]):
    matrix2.append([int(el) for el in input().split()])

matrix_res = list()
for rows in range(len(matrix1)):
    temp = list()
    for col_m2 in range(len(matrix2[0])):
        sum_el = 0
        for el in range(len(matrix1[0])):
            sum_el += matrix1[rows][el] * matrix2[el][col_m2]
        temp.append(sum_el)
    matrix_res.append(temp)

for row in matrix_res:
    print(*row)
