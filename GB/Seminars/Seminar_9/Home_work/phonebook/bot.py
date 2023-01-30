import telebot
import working_with_datebase as wd


bot = telebot.TeleBot('5841865362:AAGe-mekNEv9gYIPrV8kxAA6eNihfpSGJrU')
chat_id = ''
surname = ''
name = ''
patronymic = ''
email_address = ''
telephone = ''


@bot.message_handler(commands=['start'])
def start(message):
    global chat_id
    chat_id = message.chat.id
    bot.send_message(chat_id, f'Привет {message.from_user.first_name}!\n'
                              f'Я умею работать с телефонным справочником.')
    bot.send_message(chat_id, 'Что будем делать?\n' 
                              '1. Добавить контакт\n'
                              '2. Найти контакт\n'
                              '3. Удалить контакт\n'
                              '4. Показать справочник\n'
                              '5. Импортировать справочник\n'
                              '6. Экспортировать справочник\n'
                              'Введи цифру!')

@bot.message_handler()
def choice(message):
    global chat_id
    chat_id = message.chat.id
    if message.text == '1':
        get_name()
    elif message.text == '2':
        bot.send_message(chat_id, 'Введите одно из данных для поиска')
        bot.register_next_step_handler(message, find_contact)
    elif message.text == '3':  # Удалить контакт
        bot.send_message(chat_id, 'Выбери контакт из списка и введи цифру!')
        bot.send_message(chat_id, wd.print_book())
        bot.register_next_step_handler(message, del_contact)
    elif message.text == '4':  # Вывод справочника
        bot.send_message(chat_id, wd.print_book())
    elif message.text == '5':  # Импорт данных из получаемого файла
        bot.send_message(chat_id, 'Отправьте мне файл .txt')
        bot.register_next_step_handler(message, import_base)
    elif message.text == '6':
        bot.send_message(chat_id, 'В каком формате отправить справочник?\n'
                                  '1. Одна запись - на одной строке;\n'
                                  '2. Каждое значение на отдельной строке\n'
                                  'Введите цифру!')
        bot.register_next_step_handler(message, export_file)
    else:
        bot.send_message(chat_id, 'Ты ввел что-то не то!')


def get_name():  # Запрашиваем имя
    mess = bot.send_message(chat_id, 'Введите имя')
    bot.register_next_step_handler(mess, get_surname)


def get_surname(mess):  # Заносим в переменную имя и запрашиваем фамилию
    global name
    name = mess.text
    bot.send_message(chat_id, 'Введите фамилию')
    bot.register_next_step_handler(mess, get_patronymic)


def get_patronymic(mess):  # Заносим в переменную фамилию и запрашиваем отчество
    global surname
    surname = mess.text
    bot.send_message(chat_id, 'Введите отчество')
    bot.register_next_step_handler(mess, get_email)


def get_email(mess):   # Заносим в переменную отчество и запрашиваем email
    global patronymic
    patronymic = mess.text
    bot.send_message(chat_id, 'Введите email')
    bot.register_next_step_handler(mess, get_telephone)


def get_telephone(mess):  # Заносим в переменную email и запрашиваем телефон
    global email_address
    email_address = mess.text
    bot.send_message(chat_id, 'Введите телефон')
    bot.register_next_step_handler(mess, set_data)


def set_data(mess):  # Заносим в переменную телефон и записываем контакт в базу
    global telephone
    telephone = mess.text
    result = wd.add_contact(surname, name, patronymic, email_address, telephone)
    if result:
        bot.send_message(chat_id, 'Контакт добавлен')

    print(wd.book)


def find_contact(mess):  # Поиск контакта в справочнике
    text = mess.text
    text = wd.find_in_book(text)
    if text:
        bot.send_message(chat_id, text)
    else:
        bot.send_message(chat_id, 'Ни чего не нашел')


def del_contact(message):  # Удаление контакта
    key = message.text
    if key.isdigit() and int(key) in wd.book.keys():
        del wd.book[int(key)]
        bot.send_message(chat_id, 'Контакт удален')
    else:
        bot.send_message(chat_id, 'Контакт не найден!')


def import_base(message):
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'E:/УЧЕБА/Python/GB/Seminars/Seminar_9/Home_work/phonebook/files/' + message.document.file_name
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    wd.import_base(src)
    bot.send_message(chat_id, 'Импорт данных завершен!')


def export_file(message):
    if message.text == '1':
        wd.ex_base(message.text)
        bot.send_document(chat_id, open(r'E:/УЧЕБА/Python/GB/Seminars/Seminar_9/Home_work/phonebook/export.csv', 'rb'))
    elif message.text == '2':
        bot.send_document(chat_id, open(r'E:/УЧЕБА/Python/GB/Seminars/Seminar_9/Home_work/phonebook/export_2.csv',
                                        'rb'))
    else:
        bot.send_message(chat_id, 'Ты что-то не то ввел')

print('Сервер запущен')
bot.polling(none_stop=True)