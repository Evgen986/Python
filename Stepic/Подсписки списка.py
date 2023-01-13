text = input().split()
result_list = [[]]
for step in range(1, len(text) + 1):
    for start_index in range(len(text)):
<<<<<<< HEAD
        if len(text)-start_index >= step:
            new_list.append(x for x in text[start_index:start_index+step])
    result_list.append(new_list)
print(result_list)

# [[], ['1', '2', '3', '0'], ['12', '23', '30'], ['123', '230'], ['1230']]
=======
        if len(text) - start_index >= step:
            result_list.append(text[start_index:start_index + step])
print(result_list)

# [[], ['1'], ['2'], ['3'], ['0'], ['1', '2'], ['2', '3'], ['3', '0'], ['1', '2', '3'], ['2', '3', '0'], ['1', '2', '3', '0']
# [[], ['1'], ['2'], ['3'], ['0'], ['1', '2'], ['2', '3'], ['3', '0'], ['1', '2', '3'], ['2', '3', '0'], ['1', '2', '3', '0']]
>>>>>>> 34142ca3a7a164f04017e9cb871c840a1b9c03ec
