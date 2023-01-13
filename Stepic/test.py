matrix = [[int(el) for el in input().split()] for rows in range(int(input()))]
maximal = matrix[0][0]
for rows in range(len(matrix)):
    for coloms in range(rows+1):
        if matrix[rows][coloms] > maximal:
            maximal = matrix[rows][coloms]
print(maximal)