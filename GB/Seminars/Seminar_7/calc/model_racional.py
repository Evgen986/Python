# Модуль расчета

def calc(my_list):
    while '*' in my_list or '/' in my_list:
        for i in range(1, len(my_list), 2):
            if my_list[i] == '*':
                result = my_list.pop(i + 1) * my_list.pop(i - 1)
                my_list[i - 1] = result
                break
            elif my_list[i] == '/':
                result = my_list.pop(i - 1) / my_list.pop(i)
                my_list[i - 1] = result
                break

    while '+' in my_list or '-' in my_list:
        for i in range(1, len(my_list), 2):
            if my_list[i] == '-':
                result = my_list.pop(i - 1) - my_list.pop(i)
                my_list[i - 1] = result
                break
            elif my_list[i] == '+':
                result = my_list.pop(i + 1) + my_list.pop(i - 1)
                my_list[i - 1] = result
                break

    return my_list


def get_result(data):
    while '(' in data:
        print(f'ищем скобки {data}')
        first_i = len(data) - data[::-1].index('(') - 1
        second_i = first_i + data[first_i + 1:].index(')') + 1
        data = data[:first_i] + calc(data[first_i + 1:second_i]) + data[second_i + 1:]
    print(f'получили новый список после скобок {data}')
    data = calc(data)
    return data

