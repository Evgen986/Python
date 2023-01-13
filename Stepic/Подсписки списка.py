text = input().replace(' ', '')
result_list = [[]]
for step in range(1, len(text)+1):
    new_list = list()
    for start_index in range(len(text)):
        if len(text)-start_index >= step:
            new_list.append(x for x in text[start_index:start_index+step])
    result_list.append(new_list)
print(result_list)

# [[], ['1', '2', '3', '0'], ['12', '23', '30'], ['123', '230'], ['1230']]