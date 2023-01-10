from random import sample


def question_yes_or_no(text):
    while True:
        rep = input(text + ' (да/нет): ')
        if rep.lower() == 'да':
            return True
        elif rep.lower() == 'нет':
            return False
        else:
            print('Моя твоя не понимает!')


def password_generation(count_p, len_p, text):
    for i in range(count_p):
        print(*sample(text, len_p), sep='')


def user_survey():
    digits = '0123456789'
    lowercase_litters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_litters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'
    chars = ''
    count_passwords = int(input('Сколько паролей необходимо сгенерировать?: '))
    len_password = int(input('Какой длины должен быть пароль?: '))
    is_digit_in_password = question_yes_or_no('Включать ли в пароль цифры?')
    if is_digit_in_password:
        chars += digits
    is_upper_in_password = question_yes_or_no('Включать ли в пароль заглавные буквы?')
    if is_upper_in_password:
        chars += uppercase_litters
    is_lower_in_password = question_yes_or_no('Включать ли в пароль строчные буквы?')
    if is_lower_in_password:
        chars += lowercase_litters
    is_punctuation_in_password = question_yes_or_no('Включать ли в пароль символы?')
    if is_punctuation_in_password:
        chars += punctuation
    exclude_ambiguous_char = question_yes_or_no('Исключать ли неоднозначные символы?')
    if exclude_ambiguous_char:
        ex_list = ['i', 'l', '1', 'L', 'o', 'O', '0']
        for el in ex_list:
            chars.replace(el, '')
    return count_passwords, len_password, chars


def main():
    cou_p, len_p, text = user_survey()
    password_generation(cou_p, len_p, text)


if __name__ == '__main__':
    main()
