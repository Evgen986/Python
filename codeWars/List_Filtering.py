def filter_list(l):
    list = []
    for i in l:
        if type(i) == int:
            list.append(i)
    return list

list1 = [1, 'a', 'b', 0, 15]
print(filter_list(list1))