# Модуль работы с пользователем
import bot_commands as bot_com


def get_nums(user_nums):  # Получение данных от пользователя
    nums = user_nums.replace('+', ' + ') \
        .replace('-', ' - ') \
        .replace('*', ' * ') \
        .replace('/', ' / ') \
        .replace('(', '( ') \
        .replace(')', ' )') \
        .replace('i', 'j') \
        .split()
    nums_list = list()
    for el in nums:
        if 'j' in el:
            nums_list.append(complex(el))
        elif el.isdigit():
            nums_list.append(int(el))
        else:
            nums_list.append(el)
    return user_nums, nums_list


def print_user(nums, data):  # Вывод данных пользователю
    print('{}={}'.format(nums, data))
