# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    
#     *Примеры:*
    
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

number = input()
if '.' not in number:
    print('нет')
else: 
    number = float(number)
    if number<0:
        number *=-1
    print(number)
    print(int(number*10%10))