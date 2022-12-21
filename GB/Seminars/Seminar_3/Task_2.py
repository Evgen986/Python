# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

def find_num(num):
    flag = False
    for item in my_list:
        if str(num) in item:
            flag = True
            break
    return flag


my_list = ['hjhjsdhj95sddf', 'sddsd', 'fdsfd', 'sdfdf', 'sdfdf']
print(find_num(68))
