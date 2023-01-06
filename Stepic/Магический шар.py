import random

answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
           'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да',
           'Да', 'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
           'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет',
           'Перспективы не очень хорошие', 'Весьма сомнительно']

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Как тебя зовут?: ')
print(f'Привет {name.capitalize()}')


def repeat():
    while True:
        rep = input('Желаешь ли еще что-то спросить (да/нет): ')
        if rep.lower() == 'да':
            return True
        elif rep.lower() == 'нет':
            return False
        else:
            print('Моя твоя не понимает!')


def main():
    flag = True
    while flag:
        text = input('Что ты хочешь спросить?: ')
        print(random.choice(answers))
        if not repeat():
            flag = False
        print('Возвращайся если возникнут вопросы!')


if __name__ == '__main__':
    main()
