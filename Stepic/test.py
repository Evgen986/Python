my_list = list()
for i in range(int(input())):
    my_list.append(input())
search_list = list()
for j in range(int(input())):
    search_list.append(input())
for index in range(len(my_list)):
    count = 0
    for ind in range(len(search_list)):
        if search_list[ind].lower() in my_list[index].lower():
            count += 1
    if count == len(search_list):
        print(my_list[index])
