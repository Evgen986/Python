n, m = [int(el) for el in input().split()]
matrix1 = list()
for _ in range(n):
    matrix1.append([int(el) for el in input().split()])

input()
matrix2 = list()
for _ in range(n):
    matrix2.append([int(el) for el in input().split()])

matrix_res = list()
for i in range(len(matrix1)):
    temp = list()
    for j in range(len(matrix1[i])):
        temp.append(matrix1[i][j] + matrix2[i][j])
    matrix_res.append(temp)

for row in matrix_res:
    print(*row)
