matrix = [['.' for el in range(8)] for rows in range(8)]
coord = input()
row = 8 - int(coord[1])
col = (ord(coord[0]) - 97)
print(len(matrix[2]))
matrix[row][col] = 'N'
for i in range(8):
    for j in range(8):
        if i == row - 2:
            if j == col - 1 or j == col + 1:
                matrix[i][j] = '*'
        if i == row - 1:
            if j == col - 2 or j == col + 2:
                matrix[i][j] = '*'
        if i == row + 1:
            if j == col - 2 or j == col + 2:
                matrix[i][j] = '*'
        if i == row + 2:
            if j == col - 1 or j == col + 1:
                matrix[i][j] = '*'

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()
