def black_or_white(pos_1, pos_2):
    if (pos_1 % 2 != 0 and pos_2 % 2 != 0) or (pos_1 % 2 == 0 and pos_2 % 2 == 0):
        return 'white'
    else:
        return 'black'


a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
color_pos_1 = black_or_white(a1, b1)
color_pos_2 = black_or_white(a2, b2)
if color_pos_1 == color_pos_2:
    print('YES')
else:
    print('NO')
