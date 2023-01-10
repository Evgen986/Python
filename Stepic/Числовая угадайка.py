import random


def is_valid(text_num):  # Функция проверки на корректность ввода
    text_num = str(text_num)
    if text_num.isdigit() and 0 < int(text_num) < 101:
        return True
    else:
        return False


def game(n1=1, n2=100):  # Функция игры
    num = random.randint(n1, n2)
    count = 0
    while True:
        num_user = input('Введите число: ')
        if is_valid(num_user):
            num_user = int(num_user)
            if num_user < num:
                count += 1
                print('Ваше число меньше загаданного, попробуйте еще разок')
            elif num_user > num:
                count += 1
                print('Ваше число больше загаданного, попробуйте еще разок')
            else:
                count += 1
                print('Вы угадали, поздравляем!')
                print(f'Вам понадобилось {count} попыток, что-бы угадать число.')
                break
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')


def repeat(text='Желаете сыграть еще раз? (да/нет): '):  # Функция повторных запросов
    while True:
        answer = input(text)
        if answer.strip().lower() == 'да':
            return True
        elif answer.strip().lower() == 'нет':
            return False
        else:
            print('Пожалуйста введите "да" или "нет"!')


def main():
    print('Добро пожаловать в числовую угадайку!')
    while True:
        if repeat(
                'По умолчанию диапазон загаданного числа от 1 до 100. Желаете задать диапазон загаданных чисел? (да/нет): '):
            game(int(input('Введите начало диапазона: ')), int(input('Введите конец диапазона: ')))
            if repeat():
                pass
            else:
                break
        else:
            game()
            if repeat():
                pass
            else:
                break
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')


if __name__ == '__main__':
    main()
