# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
# new_list = list()
# for dic in users:
#     if len(dic) > 2:
#         if len(dic['email']) == 0:
#             new_list.append(dic['name'])
#     else:
#         new_list.append(dic['name'])
# print(*sorted(new_list))

# d = {
#     0: "zero",
#     1: "one",
#     2: "two",
#     3: "three",
#     4: "four",
#     5: "five",
#     6: "six",
#     7: "seven",
#     8: "eight",
#     9: "nine"
# }
# num = input()
# for el in num:
#     print(d[int(el)], end=' ')

# d = {
#     "CS101": "3004, Хайнс, 8:00",
#     "CS102": "4501, Альварадо, 9:00",
#     "CS103": "6755, Рич, 10:00",
#     "NT110": "1244, Берк, 11:00",
#     "CM241": "1411, Ли, 13:00"
# }
# key = input()
# print(f'{key}: {d[key]}')

# text = input().split()
# my_dict = {}
# new_list = list()
# for el in text:
#     if el not in my_dict.keys():
#         my_dict[el] = 0
#         new_list.append(el)
#     else:
#         my_dict[el] += 1
#         new_list.append(el + '_' + str(my_dict[el]))
# print(*new_list)

# book = {el.split() for el in input().split(':') for _ in range(int(input()))}
# 5
# Змея: язык программирования Python
# Баг: от англ. bug — жучок, клоп, ошибка в программе
# Конфа: конференция
# Костыль: код, который нужен, чтобы исправить несовершенство ранее написанного кода
# Бета: бета-версия, приложение на стадии публичного тестирования
# 3
# Змея
# Жаба
# костыль
# book = {}
# for i in range(int(input())):
#     text = input().lower().split(':')
#     book[text[0].lower()] = text[1].lstrip()
# for _ in range(int(input())):
#     print(book.get(input().lower(), 'Не найдено'))

book = {k: el for _ in range(int(input())) for k, el in [input().split(' ', 1)]}

# if text in book.keys():
#     print(book.get(text))
# else:
for _ in range(int(input())):
    for key in book.keys():
        text = input()
        if text in book[key]:
            print(key)
print(book)