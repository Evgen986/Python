# import time
# from random import randint
# import re
#
#
# def get_num(min_num, max_num, even):
#     if even:
#         num = 1
#         while num % 2:
#             num = randint(min_num, max_num)
#         return num
#     else:
#         num = 2
#         while not num % 2:
#             num = randint(min_num, max_num)
#         return num
#
#
# book = {}
# surname = ['Щученко', 'Иванько', 'Демченко', 'Пономаренко', 'Харченко', 'Семененко', 'Коваленко', 'Федоренко']
# name = ['Александр', 'Светлана', 'Сергей', 'Екатерина', 'Петр', 'Инга', 'Леонид', 'Ирина']
# patronymic = ['Петрович', 'Семеновна', 'Сергеевич', 'Ивановна', 'Егорович', 'Петровна', 'Иванович', 'Сергеевна']
# email_login = ['user_1', 'user_2', 'user_3', 'user_4', 'user_5', 'user_6', 'user_7', 'user_8']
# email_domain = ['@mail.ru', '@yandex.ru', '@gmail.com', '@mail.com', '@rambler.ru', '@yandex.com']
# for i in range(len(book)+1, randint(6, 10)):
#     book[i] = dict(zip(['surname', 'name', 'patronymic', 'email', 'telephone'],
#                        [surname[randint(0, 7)], name[get_num(0, 7, i % 2)], patronymic[get_num(0, 7, i % 2)],
#                         ''.join(email_login[randint(0, 7)] + email_domain[randint(0, 5)]),
#                         '+7-' + str(randint(900, 999)) + '-' + str(randint(100, 999)) + '-'
#                         + str(randint(10, 99)) + '-' + str(randint(10, 99))]))
#     print(' '.join(book[i].values()))
# book[5] = {'surname': 'Щученко', 'name': 'Александр', 'patronymic': 'Петрович', 'email': 'user_1' + '@mail.ru',
#            'email_1': 'g@mail.com', 'telephone': '+7-999-999-99-99'}
# book[5].update({'email_2': 'f@mail.ru'})
# for key in book.keys():
#     if 'Щученко' in book[key].values() and 'Александр' in book[key].values() and 'Петрович' in book[key].values():
#         print('да')
#
# # print(' '.join(list(book[5].keys())).count('email')) # Посчитать кол-во ключей
# # print('g@mail.com' in book[5].values())
# print(book)

list = [1]
print(list[0])