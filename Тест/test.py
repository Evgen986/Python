book = {1: {'surname': 'Иванов', 'name': 'Иван', 'patronymic': 'Иванович', 'email': '123@mail.ru',
            'telephone': '+7-911-010-10-10'}}

my_list = list()
my_list.append(' '.join(book[1].values()))
print(my_list)
