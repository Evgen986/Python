text = input().split()
result_list = [[]]
for step in range(1, len(text) + 1):
    for start_index in range(len(text)):
        if len(text) - start_index >= step:
            result_list.append(text[start_index:start_index + step])
print(result_list)

# [[], ['1'], ['2'], ['3'], ['0'], ['1', '2'], ['2', '3'], ['3', '0'], ['1', '2', '3'], ['2', '3', '0'], ['1', '2', '3', '0']
# [[], ['1'], ['2'], ['3'], ['0'], ['1', '2'], ['2', '3'], ['3', '0'], ['1', '2', '3'], ['2', '3', '0'], ['1', '2', '3', '0']]
