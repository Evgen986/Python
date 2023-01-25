import user_interface as ui
import working_data as wd

data_workers = {}
data_departments = {}


user_choice = ui.user_choose()  # Получаем выбор пользователя
if user_choice == '9':  # Если получена команда "9" - выходим из программы
    exit()

with open('data_workes.txt', encoding='utf=8') as dw_file:  # Импортируем базу данных СОТРУДНИКОВ из файла
    for line in dw_file:
        data_workers[line[0]] = [el.rstrip('\n') for el in line[1:].split('*') if len(el) > 0]

with open('data_department.txt', encoding='utf=8') as dd_file:  # Импортируем базу данных ОТДЕЛОВ из файла
    for line in dd_file:
        data_departments[line[0]] = [el.rstrip('\n') for el in line[1:].split('*') if len(el) > 0]
        data_departments[line[0]].append(data_departments[line[0]].pop().split('%'))

while user_choice != '9':  # Цикл пока не получен "0" - выход

    if user_choice == '1':  # Добавить сотрудника
        data_workers, data_departments = wd.add_worker(data_workers, data_departments)

    elif user_choice == '2':  # Добавить отдел
        pass

    elif user_choice == '3':  # Редактировать сотрудника
        pass

    elif user_choice == '4':  # Редактировать отдел
        pass

    elif user_choice == '5':  # Удалить сотрудника
        pass

    elif user_choice == '6':  # Удалить отдел
        pass

    elif user_choice == '7':  # Вывести в консоль
        print('База сотрудников:')
        for key in data_workers:
            print(key + ' - ', end='')
            print(*data_workers[key], sep='; ', end=';\n')
        print('\nБаза отделов')
        for key in data_departments:
            print(key + ' - ', end='')
            print(*data_departments[key], sep='; ', end=';\n')
        print()

    elif user_choice == '8':  # Экспорт
        pass

    elif user_choice == '9':  # Выход
        pass
    user_choice = ui.user_choose()