a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
a_d = a2-a1
b_d = b2-b1
if a_d < 0:
    a_d *= -1
if b_d < 0:
    b_d *= -1
if (a_d == 1 and b_d == 1) or (a_d == 0 and b_d > 0 or a_d > 0 and b_d == 0) or (a_d == b_d):
    print('YES')
else:
    print('NO')
