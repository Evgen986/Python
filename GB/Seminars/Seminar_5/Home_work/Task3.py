# Создайте программу для игры в ""Крестики-нолики"".
import Task2
import random


def print_dic(dicti):  # Печать матрицы
    print(' ' + dicti['1'], dicti['2'], dicti['3'], sep=' | ')
    print('-' * 11)
    print(' ' + dicti['4'], dicti['5'], dicti['6'], sep=' | ')
    print('-' * 11)
    print(' ' + dicti['7'], dicti['8'], dicti['9'], sep=' | ')
    print()


def check_winner(dicti): # Проверка победителя
    if (dicti.get('1') == '0' and dicti.get('2') == '0' and dicti.get('3') == '0') or \
            (dicti.get('1') == 'x' and dicti.get('2') == 'x' and dicti.get('3') == 'x') or \
            (dicti.get('4') == '0' and dicti.get('5') == '0' and dicti.get('6') == '0') or \
            (dicti.get('4') == 'x' and dicti.get('5') == 'x' and dicti.get('6') == 'x') or \
            (dicti.get('7') == '0' and dicti.get('8') == '0' and dicti.get('9') == '0') or \
            (dicti.get('7') == 'x' and dicti.get('8') == 'x' and dicti.get('9') == 'x') or \
            (dicti.get('1') == '0' and dicti.get('5') == '0' and dicti.get('9') == '0') or \
            (dicti.get('1') == 'x' and dicti.get('5') == 'x' and dicti.get('9') == 'x') or \
            (dicti.get('3') == '0' and dicti.get('5') == '0' and dicti.get('7') == '0') or \
            (dicti.get('3') == 'x' and dicti.get('5') == 'x' and dicti.get('7') == 'x') or \
            (dicti.get('3') == '0' and dicti.get('6') == '0' and dicti.get('9') == '0') or \
            (dicti.get('3') == 'x' and dicti.get('6') == 'x' and dicti.get('9') == 'x') or \
            (dicti.get('2') == '0' and dicti.get('5') == '0' and dicti.get('8') == '0') or \
            (dicti.get('2') == 'x' and dicti.get('5') == 'x' and dicti.get('8') == 'x') or \
            (dicti.get('1') == '0' and dicti.get('4') == '0' and dicti.get('7') == '0') or \
            (dicti.get('1') == 'x' and dicti.get('4') == 'x' and dicti.get('7') == 'x'):
        return True
    else:
        return False


def game_people(first_p):  # Игра с человеком
    player_list = ['Игрок №2', 'Игрок №1']
    player = first_p
    dic = {'1': '.', '2': '.', '3': '.', '4': '.', '5': '.', '6': '.', '7': '.', '8': '.', '9': '.'}
    while True:
        print_dic(dic)
        player_takes = input(f'{player_list[player]} выберите клетку: ')
        if player_takes.isdigit() and 0 < int(player_takes) < 10 and dic.get(player_takes) == '.':
            if player:
                dic[player_takes] = 'x'
            else:
                dic[player_takes] = '0'
        else:
            print('Убедитесь в корректности ввода!')
        if check_winner(dic):
            print(f'Игра окончена! Победитель {player_list[player]}, поздравляем!')
            exit()
        else:
            player = not player


def game_pc(first_p):  # Игра против ПК
    player_list = ['Компьютер', 'Игрок №1']
    player = first_p
    dic = {'1': '.', '2': '.', '3': '.', '4': '.', '5': '.', '6': '.', '7': '.', '8': '.', '9': '.'}
    while True:
        if player:
            player_takes = input(f'{player_list[player]} выберите клетку: ')
            if player_takes.isdigit() and 0 < int(player_takes) < 10 and dic.get(player_takes) == '.':
                if player:
                    dic[player_takes] = 'x'
            else:
                print('Убедитесь в корректности ввода!')
        else:
            print('Ход компьютера:')
            flag = True
            while flag:
                pc_takes = random.randint(1, 9)
                if dic[str(pc_takes)] == '.':
                    dic[str(pc_takes)] = '0'
                    flag = False
        print_dic(dic)
        if check_winner(dic):
            print(f'Игра окончена! Победитель {player_list[player]}, поздравляем!')
            exit()
        else:
            player = not player


def main():
    print('Приветствуем Вас в игре крестики-нолики!\nПожалуйста ознакомьтесь с таблицей для выбора ячеек!')
    print(' ' + '1', '2', '3', sep=' | ')
    print('-' * 11)
    print(' ' + '4', '5', '6', sep=' | ')
    print('-' * 11)
    print(' ' + '7', '8', '9', sep=' | ', end='\n\n')
    player = Task2.choice_player()  # Человек - True, Компьютер - False
    print(player)
    if not player:  # Если игра против ПК
        first = Task2.first_player(0)  # Игрок 1 - True, Игрок2(ПК) - False
        print(first)
        game_pc(first)
    else:  # Если играют люди
        game_people(Task2.first_player(0))


if __name__ == '__main__':
    main()
