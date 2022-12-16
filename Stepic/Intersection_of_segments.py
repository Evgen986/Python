a1, a2, b1, b2 = int(input()), int(input()), int(input()), int(input())
if a2==b1:
    print(a2)
elif a1==b2:
    print(a1)
elif b1>a2:
    print(b1, a2)
elif b2>a1:
    print(a1, b2)
else:
    print('пустое множество')