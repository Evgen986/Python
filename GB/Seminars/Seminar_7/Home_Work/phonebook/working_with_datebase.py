# Модуль работы с БД
from random import randint
import log_generate as lg


def get_num(min_num, max_num, even): # Функция получения рандомных значений для заполнения справочника
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


def find_in_book(f_book: dict):  # Функция поиска в справочнике
    lg.write_data('Запущен поиск по справочнику;')
    f_num = 0  # Значение выбора пользователя для поиска
    while True:
        f_num = input('Выберите вариант поиска:\n'
                      '1 - По коду строки\n'
                      '2 - По фамилии\n'
                      '3 - По имени\n'
                      '4 - По отчеству\n'
                      '5 - По email\n'
                      '6 - По номеру телефона')
        if f_num in ['1', '2', '3', '4', '5', '6']:
            lg.write_data('Пользователь ввел команду: ' + f_num)
            break
        else:
            lg.write_data('Введено некорректное значение: ' + f_num)
            print('Проверьте корректность ввода!')
    while True:
        if f_num == '1':
            f_choice = input('Введите код строки: ')
            if int(f_choice) in f_book.keys():
                return int(f_choice)
            else:
                print('Проверьте корректность ввода!')
                # continue
        elif f_num == '2':
            f_choice = input('Введите фамилию: ')
            choice_list = list()
            for key in f_book:
                if f_choice in f_book[key].values():
                    choice_list.append(key)
            if len(choice_list) == 0:
                print('Проверьте корректность ввода!')
                continue
            elif len(choice_list) > 1:
                for el in choice_list:
                    print(str(el) + ' - ', end='')
                    print(*f_book[el].values())
                f_choice = input('Введите код строки: ')
                if int(f_choice) in choice_list:
                    return int(f_choice)
                else:
                    print('Проверьте корректность ввода!')
            else:
                return choice_list[0]
        elif f_num == '3':
            pass
        elif f_num == '4':
            pass
        elif f_num == '5':
            pass
        else:
            pass


def work_db(command, book: dict):  # Основная функция работы со справочником
    if command == 1:  # 1. Сгенерировать случайный справочник
        lg.write_data('Начато создание рандомного справочника;')
        surname = ['Щученко', 'Иванько', 'Демченко', 'Пономаренко', 'Харченко', 'Семененко', 'Коваленко', 'Федоренко']
        name = ['Александр', 'Светлана', 'Сергей', 'Екатерина', 'Петр', 'Инга', 'Леонид', 'Ирина']
        patronymic = ['Петрович', 'Семеновна', 'Сергеевич', 'Ивановна', 'Егорович', 'Петровна', 'Иванович', 'Сергеевна']
        email_login = ['user_1', 'user_2', 'user_3', 'user_4', 'user_5', 'user_6', 'user_7', 'user_8']
        email_domain = ['@mail.ru', '@yandex.ru', '@gmail.com', '@mail.com', '@rambler.ru', '@yandex.com']
        for i in range(len(book)+1, randint(5, 10)):
            book[i] = dict(zip(['surname', 'name', 'patronymic', 'email', 'telephone'],
                               [surname[randint(0, 7)], name[get_num(0, 7, i % 2)], patronymic[get_num(0, 7, i % 2)],
                                ''.join(email_login[randint(0, 7)]+email_domain[randint(0, 5)]),
                                '+7-' + str(randint(900, 999)) + '-' + str(randint(100, 999)) + '-'
                                + str(randint(10, 99)) + '-' + str(randint(10, 99))]))
            lg.write_data('Создана запись: ' + ' '.join(book[i].values()) + ';')
        lg.write_data('Создание справочника завершено;')
        return book

    elif command == 2:  # 2. Ввести данные в справочник
        surname = input('Введите фамилию: ')
        name = input('Введите имя: ')
        patronymic = input('Введите отчество: ')
        email_address = input('Введите email: ')
        telephone = input('Введите телефон в формате +7-000-000-00-00: ')
        lg.write_data('От пользователя получены данные: ' + surname + ' ' + name + ' ' + patronymic  # Запись в лог
                      + ' ' + email_address + ' ' + telephone + ';')
        flag = True # Флаг для проверки на наличие дублей в справочнике
        for key in book.keys():  # Проверка на наличие совпадений в справочнике
            if surname in book[key].values() and name in book[key].values() and patronymic in book[key].values():
                lg.write_data('Обнаружено совпадение!')
                choice = True
                flag = False
                while choice:
                    choice = input('В справочнике обнаружена запись с совпадающими ФИО\n'
                                   'Хотите обновить запись (''да/нет)?: ')
                    if choice == 'да':
                        lg.write_data('Пользователь обновляет запись;')
                        if email_address not in book[key].values() and len(email_address) > 0:  # Если email в ячейке
                            # словаря не найден
                            count = ' '.join(list(book[key].keys())).count('email') # Проверяем кол-во ключей с
                            # именем email
                            book[key].update({'email_'+str(count): email_address}) # Создаем новую пару ключ: адрес
                            lg.write_data('В словарь добавлен новый email;')
                        if telephone not in book[key].values() and len(telephone) > 0:
                            count = ' '.join(list(book[key].keys())).count('telephone')  # Проверяем кол-во ключей с
                            # именем telephone
                            book[key].update({'telephone_' + str(count): telephone})  # Создаем новую пару ключ: телефон
                            lg.write_data('В словарь добавлен новый телефон;')
                        choice = False  # Меняем choiсe на True, что-бы выйти из while
                    elif choice == 'нет':
                        choice = False  # Меняем choiсe на True, что-бы выйти из while
                        flag = True  # Меняем флаг на True для создания новой записи
                    else:
                        lg.write_data(f'Введены некорректные данные - "{choice}";')
                        choice = True  # Если введено отличное от да/нет то меняем choice на False, что бы цикл
                        # продолжался
        if flag:  # Если дублей в справочнике не найдено или пользователь решил создать новую запись
            book[len(book) + 1] = dict(zip(['surname', 'name', 'patronymic', 'email', 'telephone'],
                                           [surname, name, patronymic, email_address, telephone]))
        lg.write_data('В справочник внесена новая запись;')
        return book

    elif command == 3:  # 3. Изменить данные в справочнике
        print('')
    elif command == 4:  # 4. Удалить данные в справочнике
        pass
    elif command == 5:  # 5. Найти данные в справочнике
        pass
    elif command == 6:  # 6. Импортировать в справочник
        pass
    elif command == 7:  # 7. Экспортировать справочник
        pass
    elif command == 8:  # 8. Показать справочник
        pass
    else:  # 9. Выход из программы
        pass
