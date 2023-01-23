# import time
from random import randint


# import re
#
#
def get_num(min_num, max_num, even):
    if even:
        num = 1
        while num % 2:
            num = randint(min_num, max_num)
        return num
    else:
        num = 2
        while not num % 2:
            num = randint(min_num, max_num)
        return num


#
#
book = {}
surname = ['Щученко', 'Иванько', 'Демченко', 'Пономаренко', 'Харченко', 'Семененко', 'Коваленко', 'Федоренко']
name = ['Александр', 'Светлана', 'Сергей', 'Екатерина', 'Петр', 'Инга', 'Леонид', 'Ирина']
patronymic = ['Петрович', 'Семеновна', 'Сергеевич', 'Ивановна', 'Егорович', 'Петровна', 'Иванович', 'Сергеевна']
email_login = ['user_1', 'user_2', 'user_3', 'user_4', 'user_5', 'user_6', 'user_7', 'user_8']
email_domain = ['@mail.ru', '@yandex.ru', '@gmail.com', '@mail.com', '@rambler.ru', '@yandex.com']
for i in range(len(book) + 1, randint(6, 10)):
    book[i] = dict(zip(['surname', 'name', 'patronymic', 'email', 'telephone'],
                       [surname[randint(0, 7)], name[get_num(0, 7, i % 2)], patronymic[get_num(0, 7, i % 2)],
                        ''.join(email_login[randint(0, 7)] + email_domain[randint(0, 5)]),
                        '+7-' + str(randint(900, 999)) + '-' + str(randint(100, 999)) + '-'
                        + str(randint(10, 99)) + '-' + str(randint(10, 99))]))
    print(str(i) + ' - ', end='')
    print(' '.join(book[i].values()))
book[5] = {'surname': 'Щученко', 'name': 'Александр', 'patronymic': 'Петрович', 'email': 'user_1' + '@mail.ru',
           'email_1': 'g@mail.com', 'telephone': '+7-999-999-99-99'}
book[5].update({'email_2': 'f@mail.ru'})

with open('export.csv', 'a', encoding='utf=8') as ex_file:
    for key in book.keys():
        ex_file.write(' '.join(list(map(str, book[key].values()))) + '\n')

with open('export_2.csv', 'a', encoding='utf=8') as ex_2_file:
    for key in book.keys():
        ex_2_file.write('\n'.join(list(map(str, book[key].values()))) + '\n\n')

# for key in book.keys():
#     if 'Щученко' in book[key].values() and 'Александр' in book[key].values() and 'Петрович' in book[key].values():
#         print('да')
#
# # print(' '.join(list(book[5].keys())).count('email')) # Посчитать кол-во ключей
# # print('g@mail.com' in book[5].values())
# print(book)
# list = [1]
# print(list[0])

# def find_in_book(f_book: dict):  # Функция поиска в справочнике возвращает ключ
#     # lg.write_data('Запущен поиск по справочнику;')
#     while True:
#         f_num = input('Выберите вариант поиска:\n'
#                       '1 - По коду строки\n'
#                       '2 - По фамилии или имени или отчеству или email или номеру телефона\n'
#                       'Введите цифру: ')
#         if f_num in ['1', '2']:
#             # lg.write_data('Пользователь ввел команду: ' + f_num)
#             break
#         else:
#             # lg.write_data('Введено некорректное значение: ' + f_num)
#             print('Проверьте корректность ввода!')
#     while True:
#         if f_num == '1':
#             f_choice = input('Введите код строки: ')
#             if int(f_choice) in f_book.keys():
#                 return int(f_choice)
#             else:
#                 print('Проверьте корректность ввода!')
#         else:
#             f_choice = input('Введите данные: ').strip().capitalize()
#             choice_list = list()
#             for key in f_book:
#                 if f_choice in f_book[key].values():
#                     choice_list.append(key)
#             if len(choice_list) == 0:
#                 print('Проверьте корректность ввода!')
#                 continue
#             elif len(choice_list) > 1:
#                 for el in choice_list:
#                     print(str(el) + ' - ', end='')
#                     print(*f_book[el].values())
#                 f_choice = input('Введите код строки: ')
#                 if int(f_choice) in choice_list:
#                     return int(f_choice)
#                 else:
#                     print('Проверьте корректность ввода!')
#             else:
#                 return choice_list[0]
#
#
# num = find_in_book(book)
# print(num)
