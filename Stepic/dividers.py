# На вход программе подается два натуральных числа aa и bb (a < ba< b).
# Напишите программу, которая находит натуральное число из отрезка [a; \, b][a;b] с максимальной суммой делителей.
# Sample Input 1:
# 1
# 10
# Sample Output 1:
# 10 18

a, b = int(input()), int(input())
sum_del = 0

for i in range(b, a - 1, -1):
    temp_sum_del = 0
    for j in range(1, i + 1):
        if i % j == 0:
            temp_sum_del += j
    if temp_sum_del > sum_del:
        sum_del = temp_sum_del
        dividers = i
print(dividers, sum_del)
