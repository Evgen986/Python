# Описание проекта:
# требуется написать программу, способную шифровать и дешифровать текст в соответствии с алгоритмом Цезаря.
# Она должна запрашивать у пользователя следующие данные:
#
# направление: шифрование или дешифрование;
# язык алфавита: русский или английский;
# шаг сдвига (со сдвигом вправо).
#
# Примечание 1. Считайте, что в русском языке 32 буквы (буква ё отсутствует).
# Примечание 2. Неалфавитные символы — знаки препинания, пробелы, цифры — не меняются.
# Примечание 3. Сохраните регистр символов. Например, текст: "Умом Россию не понять" при сдвиге на одну позицию вправо
#                                                                       будет преобразован в: "Фнпн Спттйя ож рпоауэ".
#
# Составляющие проекта:
#
# Целые числа (тип int);
# Модульная арифметика;
# Переменные;
# Ввод / вывод данных (функции input() и print());
# Условный оператор (if/elif/else);
# Цикл for/while;
# Строковые методы.

def code_decod():
    while True:
        indication = input('Введите "код" для кодирования, "декод" для декодирования: ')
        if indication == 'код':
            return True
        elif indication == 'декод':
            return False
        else:
            print('Некорректный ввод!')


def language():
    while True:
        indication = input('Выберите язык "англ" - английский, "рус" - русский: ')
        if indication == 'англ':
            return True
        elif indication == 'рус':
            return False
        else:
            print('Некорректный ввод!')


def coding(text: str, coding, language, step):
    if language:
        lower_alph = 'abcdefghijklmnopqrstuvwxyz'
        result = ''
        if coding:
            for el in text:
                if not el.isalpha():
                    result += el
                else:
                    result += lower_alph[(lower_alph.find(el.lower()) + step) % len(lower_alph)]
        else:
            for el in text:
                if not el.isalpha():
                    result += el
                else:
                    result += lower_alph[(lower_alph.find(el.lower()) - step) % len(lower_alph)]
        for index in range(len(text)):
            if text[index].isupper():
                result = result[:index] + result[index].upper() + result[index + 1:]
    else:
        lower_alph = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        result = ''
        if coding:
            for el in text:
                if not el.isalpha():
                    result += el
                else:
                    result += lower_alph[(lower_alph.find(el.lower()) + step) % len(lower_alph)]
        else:
            for el in text:
                if not el.isalpha():
                    result += el
                else:
                    result += lower_alph[(lower_alph.find(el.lower()) - step) % len(lower_alph)]
        for index in range(len(text)):
            if text[index].isupper():
                result = result[:index] + result[index].upper() + result[index + 1:]
    return result


text = input('Введите текст: ')
cod = code_decod()
lang = language()
step = int(input('Введите шаг сдвига: '))
print(coding(text, cod, lang, step))

# print(ord('А'))
# print(ord('Я'))
# print(ord('а'))
# print(ord('я'))
#
# print(f'ind {(0 - 3) % 33}')
