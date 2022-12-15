# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

xyz = ["X", "Y", "Z"]
my_list = []
for i in range(len(xyz)):
    my_list.append(input(f"Введите значение {xyz[i]}: "))

left = not (my_list[0] or my_list[1] or my_list[2])
right = not my_list[0] and not my_list[1] and not my_list[2]
result = left == right

if result == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")
