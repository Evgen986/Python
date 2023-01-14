matrix = [[int(el) for el in input().split()] for rows in range(int(input()))]
pow_list = int(input())
res_list = [el.copy() for el in matrix]
while pow_list > 1:
    for rows in range(len(res_list)):
        temp = list()
        for col_m2 in range(len(matrix[0])):
            sum_el = 0
            for el in range(len(res_list[0])):
                sum_el += res_list[rows][el] * matrix[el][col_m2]
            temp.append(sum_el)
        res_list[rows] = temp
    pow_list -= 1

for row in res_list:
    print(*row)
