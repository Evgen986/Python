# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

import random


def choice_player():
    while True:
        choice = input('С кем бы Вы хотели играть? Человек или компьютер?:\n')
        if choice.lower() == 'человек':
            return True
        elif choice.lower() == 'компьютер':
            return False
        elif choice == 'выход':
            exit()
        else:
            print('Пожалуйста убедитесь, что Вы ввели "человек" или "компьютер"!\nДля выхода из игры введите "выход".')


def selection_difficulty():
    while True:
        selection = input('Выберите уровень сложности!\n1. Простой\n2. Средний\n3. Сложный\nВведите цифру: ')
        if selection.isdigit() and 0 < int(selection) < 4:
            return int(selection)
        else:
            print('Пожалуйста убедитесь, что Вы ввели корректную цифру!')


def first_player(diff):  # Определяем кто первый ходит
    while True:
        coin_side = ['орел', 'решка']
        coin = input('Подбросим монетку, что бы определить кто первый ходит. Игрок №1 выберите "орел" или "решка"?:\n')
        if coin.lower() in coin_side:
            if diff == 3:  # Если сложность №3
                side = coin_side[not bool(coin_side.index(coin))]  # Получаем сторону противоположную выбору игрока
                print(f'К сожалению у Вас {side}. Компьютер ходит первый.')
                return False
            else:
                side = coin_side[random.randint(0, 1)]
                if side in coin:
                    print(f'Поздравляем! У Вас {side}. Вы ходите первый')
                    return True
                else:
                    print(f'К сожалению у Вас {side}. Противник ходит первый.')
                    return False
        else:
            print('Пожалуйста убедитесь, что Вы ввели "орел" или "решка"!')


def main():
    player = choice_player()  # Человек - True, Компьютер - False
    print(player)
    if not player:
        difficulty = selection_difficulty()  # Сложность 1-пк поддается, 2-рандом, 3-пк выигрывает
        print(difficulty)
    else:
        difficulty = 0
    first = first_player(difficulty)  # Игрок 1 - True, Игрок2(ПК) - False
    print(first)


if __name__ == '__main__':
    main()
