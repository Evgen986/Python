# 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

def find_index_coin(new_list, text, num=2):
    count = 0
    for i in range(len(new_list)):
        if text == new_list[i]:
            count += 1
            if count == num:
                return i
    return -1


my_list = ["qwe", "qwe", "asd", "qwe", "zxc", "qwe", "ertqwe", "qwe"]
print(find_index_coin(my_list, 'qwe'))
