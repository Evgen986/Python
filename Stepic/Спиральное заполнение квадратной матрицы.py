size = [int(el) for el in input().split()]  # Получаем размеры матрицы
matrix = [[0] * size[1] for rows in range(size[0])]  # Создаем пустую матрицу заполненную нулями
counter = 1  # Счетчик для заполнения матрицы

for index in range(len(matrix[0])):  # Заполняем верхнюю строку матрицы от начала к концу
    matrix[0][index] = counter
    counter += 1
if size[0] > 1 and size[1] > 1:  # Если матрица больше одной строки и одной колонки
    for index in range(1, len(matrix)):  # Заполняем правую сторону матрицы сверху вниз
        matrix[index][-1] = counter
        counter += 1

    for index in range(len(matrix[-1]) - 2, -1, -1):  # Заполняем нижнюю строку матрицы от конца к началу
        matrix[-1][index] = counter
        counter += 1

    for index in range(len(matrix) - 2, 0, -1):  # Заполняем левую сторону матрицы от низа к верху
        matrix[index][0] = counter
        counter += 1

    ind_row = 1  # Задаем контрольную точку на строке для заполнения внутренней части матрицы
    ind_el = 1  # Задаем контрольную точку на элементе для заполнения внутренней части матрицы

    while len(matrix) * len(matrix[0]) - counter >= 1:  # Пока счетчик не будет на 1 меньше чем размер матрицы
        while matrix[ind_row][ind_el + 1] == 0:  # Пока значение справа равно нулю заполнять матрицу
            matrix[ind_row][ind_el] = counter
            counter += 1
            ind_el += 1
        while matrix[ind_row + 1][ind_el] == 0:  # Пока значение снизу равно нулю заполнять матрицу
            matrix[ind_row][ind_el] = counter
            counter += 1
            ind_row += 1
        while matrix[ind_row][ind_el - 1] == 0:  # Пока значение слева равно нулю заполнять матрицу
            matrix[ind_row][ind_el] = counter
            counter += 1
            ind_el -= 1
        while matrix[ind_row - 1][ind_el] == 0:  # Пока значение сверху равно нулю заполнять матрицу
            matrix[ind_row][ind_el] = counter
            counter += 1
            ind_row -= 1
elif size[1] == 1:  # Ели колонка одна
    for index in range(len(matrix) - 1):  # Заполняем колонку вниз, за исключением первой строки
        matrix[index + 1][0] = counter
        counter += 1

for in_r in range(len(matrix)):  # Находим и заполняем последний элемент матрицы
    for ind_e in range(len(matrix[in_r])):
        if matrix[in_r][ind_e] == 0:
            matrix[in_r][ind_e] = counter

for row in matrix:  # Печать матрицы
    for el in row:
        print(str(el).ljust(3), end='')
    print()
