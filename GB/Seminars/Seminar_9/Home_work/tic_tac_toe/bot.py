import telebot
import game

bot = telebot.TeleBot('5841865362:AAGe-mekNEv9gYIPrV8kxAA6eNihfpSGJrU')
chat_id = ''
dic = {'1': '.', '2': '.', '3': '.', '4': '.', '5': '.', '6': '.', '7': '.', '8': '.', '9': '.'}


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}!')
    bot.send_message(message.chat.id, 'Я еще только учусь и знаю несколько слов:\nпоиграем\nпомощь')
    bot.send_message(message.chat.id, f'Чем займемся?')


@bot.message_handler()
def get_user_text(message):
    mes = message
    if mes.text == 'game':
        global chat_id
        chat_id = mes.chat.id
        bot.send_message(chat_id, 'Класс! Я умею играть в крестики-нолики!')
        bot.send_message(chat_id, 'Давай играть! Чур у меня нолики! Хочешь ходить первым?')
        global dic
        dic = {'1': '.', '2': '.', '3': '.', '4': '.', '5': '.', '6': '.', '7': '.', '8': '.', '9': '.'}
        bot.register_next_step_handler(mes, start_game)
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю! Может ты хотел сказать: "поиграем"?')


def start_game(message):
    if message.text == 'да':
        bot.send_message(chat_id, 'Выбери клетку!')
        bot.register_next_step_handler(message, user_check)
    elif message.text == 'нет':
        bot.send_message(chat_id, 'Хорошо, я начинаю!')
        pc_check()
    else:
        bot.send_message(chat_id, 'Я тебя не пониманию! Скажи еще раз!')
        bot.register_next_step_handler(message, start_game)


def user_check(message):
    global dic
    player_turn = message.text
    if player_turn in ('1', '2', '3', '4', '5', '6', '7', '8', '9') and dic.get(player_turn) == '.':
        dic[player_turn] = 'x'
        if game.check_winner(dic):
            bot.send_message(chat_id, 'Ты выиграл!')
        elif '.' not in dic.values():
            bot.send_message(chat_id, 'Ой у нас ничья!')
        else:
            bot.send_message(chat_id, game.print_dic(dic))
            pc_check()
    else:
        bot.send_message(chat_id, 'Ты что-то не то ввел! Попробуй еще раз!')
        bot.register_next_step_handler(message, user_check)


def pc_check():
    global dic
    bot.send_message(chat_id, 'Мой ход:')
    dic[game.pc_choice(dic)] = '0'
    bot.send_message(chat_id, game.print_dic(dic))
    if game.check_winner(dic):
        bot.send_message(chat_id, 'Я победил!')
    elif '.' not in dic.values():
        bot.send_message(chat_id, 'Ой у нас ничья!')
    else:
        message = bot.send_message(chat_id, 'Твой ход!')
        bot.register_next_step_handler(message, user_check)


print('Сервер запущен')
bot.polling(none_stop=True)
