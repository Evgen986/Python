# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# (1+2)*3=9

s = '(10+12)*3'
num = ''
my_list = []
for elem in s:
    if elem == '(' or elem == ')':
        my_list.append(elem)
        continue
    if elem.isdigit():
        num += elem
    else:
        my_list.append(int(num))
        my_list.append(elem)
        num = ''
my_list.append(int(num))

for i in range(1, len(my_list), 2):
    if my_list[i] == '*':
        result = my_list.pop(i + 1) * my_list.pop(i - 1)
        my_list[i - 1] = result
    elif my_list[i] == '/':
        result = my_list.pop(i + 1) / my_list.pop(i - 1)
        my_list[i - 1] = result

for i in range(1, len(my_list), 2):
    if my_list[i] == '-':
        result = my_list.pop(i + 1) - my_list.pop(i - 1)
        my_list[i - 1] = result
    elif my_list[i] == '+':
        result = my_list.pop(i + 1) + my_list.pop(i - 1)
        my_list[i - 1] = result

print(my_list)

