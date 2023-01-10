def pascal(num):
    pascal_list = [[1], [1, 1]]
    for lines in range(2, num+1):
        new_line = [1]
        for el in range(1, lines):
            new_line.append(pascal_list[lines-1][el-1] + pascal_list[lines-1][el])
        new_line.append(1)
        pascal_list.append(new_line)
    return pascal_list[num]


n = int(input())
print(pascal(n))