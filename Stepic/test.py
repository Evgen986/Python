set_1 = set(int(el) for el in input().split())
set_2 = set(int(el) for el in input().split())
set_3 = set(int(el) for el in input().split())
print(*sorted(set_1 ^ set_2 ^ set_3))

