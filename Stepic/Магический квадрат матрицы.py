matrix = [[int(el) for el in input().split()] for rows in range(int(input()))]
matrix_test = list()
list_sum = list()
len_list, sum_d1, sum_d2 = 0, 0, 0

for x in matrix:  # Проверка на последовательность
    matrix_test.extend(x)
    len_list += len(x)
matrix_test = list(set(matrix_test))
if len_list == len(matrix_test) and matrix_test.count(0) == 0:
    for i in range(len(matrix)):  # Проверка строк, столбцов, диагоналей
        list_sum.append(sum(matrix[i]))
        sum_d1 += matrix[i][i]
        sum_d2 += matrix[len(matrix) - 1 - i][i]
    for i in range(len(matrix)):
        sum_c = 0
        for j in range(len(matrix[i])):
            sum_c += matrix[j][i]
        list_sum.append(sum_c)
    list_sum.append(sum_d1)
    list_sum.append(sum_d2)
    for i in range(1, len(list_sum)):  # Сравнение полученных результатов
        if list_sum[0] != list_sum[i]:
            print('NO')
            break
    else:
        print('YES')
else:
    print('NO')
