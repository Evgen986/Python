
def add_department(department_base: dict):
    name_department = input('Введите название отдела')
    department_base[str(len(department_base)+1)] = [name_department, '', []]
    return department_base

def add_worker(base_workers: dict, base_department: dict):  # Функция добавления работника
    surname = input('Введите фамилию сотрудника: ').strip().capitalize()
    name = input('Введите имя сотрудника: ').strip().capitalize()
    patronymic = input('Введите отчество сотрудника: ').strip().capitalize()
    telephone = input('Введите телефон сотрудника: ').strip()
    address = input('Введите адрес проживания сотрудника: ').strip()
    position = input('Введите должность сотрудника: ').strip()

    print('Выберите отдел из списка и введите ключ, что-бы создать новый отдел - введите "n".')
    for key in base_department:  # Выводим отделы пользователю
        print(f'{key} - {base_department[key][0]}')
    department = input('Введите отдел: ').strip().lower()

    while department not in [el for el in base_department.keys()] + ['n']:  # Проверка на корректность ввода
        print('Не корректный ввод!')
        department = input('Введите отдел: ').strip().lower()

    if department == 'n':  # Если пользователь решил создать новый отдел
        base_department = add_department(base_department)
        base_workers[str(len(base_workers) + 1)] = [surname, name, patronymic, telephone, address, position, department]
        base_department[str(len(base_department))][2].append(str(len(base_workers)))
        base_department[str(len(base_department))][1] = str(len(base_department[department][2]))
    else:  # Если пользователь выбрал существующий отдел
        # Заносим нового сотрудника в базу сотруднников
        base_workers[str(len(base_workers)+1)] = [surname, name, patronymic, telephone, address, position, department]
        # Добавляем id сотрудника в базу отделов
        base_department[department][2].append(str(len(base_workers)))
        # Изменяем количество сотрудников в отделе
        base_department[department][1] = str(len(base_department[department][2]))
        return base_workers, base_department
