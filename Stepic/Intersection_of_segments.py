a1, a2, b1, b2 = int(input()), int(input()), int(input()), int(input())
if a1<b1:
    if a2==b1:
        print(a2)
    elif a2>b1 and (b2>a2 or b2==a2):
        print(b1, a2)
    elif a2>b1 and b2<a2:
        print(b1, b2)
    else:
        print('пустое множество')
else:
    if b2==a1:
        print(b2)
    elif b2>a1 and (a2>b2 or b2==a2):
        print(a1, b2)
    elif b2>a1 and a2<b2:
        print(a1, a2)
    else:
        print('пустое множество')