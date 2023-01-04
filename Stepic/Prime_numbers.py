# На вход программе подается два натуральных числа a и b (a < b).
# Напишите программу, которая находит все простые числа от a до b включительно

num = int(input())
num_2 = int(input())
if num > 0 and num_2 < 3:
    print(2)
elif num > 0 and num_2 < 4:
    print(2, 3, sep='\n')
else:
    for i in range(num, num_2 + 1):
        if i == 1:
            continue
        count = 0
        for j in range(2, i):
            if j != i and i % j == 0:
                count += 1
        if count == 0:
            print(i)
