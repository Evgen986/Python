num = int(input())
n = 0
n_1 = 1
print(n_1, end=' ')
for i in range(1, num):
    n, n_1 = n_1, n + n_1
    print(n_1, end=' ')
