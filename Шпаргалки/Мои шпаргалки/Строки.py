text = '   heLlo woRld!***'  # строка для тестов

#                           КОНВЕРТАЦИЯ РЕГИСТРА

cap = text.capitalize()  # Возвращает копию строки, в которой: первый символ имеет верхний регистр, а все остальные нижний регистр
print(f'text.capitalize() = {cap}')  # результат = Hello world!

swap = text.swapcase()  # Возвращает копию строки, в которой: символы имеют зеркальный регистр
print(f'text.swapcase() = {swap}')  # результат = HElLO WOrLD!

t = text.title()  # Возвращает копию строки, в которой: первый символ каждого слова в верхнем регистре
print(f'text.title() = {t}')  # результат = Hello World!

low = text.lower()  # Возвращает копию строки, в которой: все символы в нижнем регистре
print(f'text.lower() = {low}')  # результат = hello world!***

upp = text.upper()  # Возвращает копию строки, в которой: все символы в верхнем регистре
print(f'text.upper() = {upp}')  # результат = HELLO WORLD!***

#                           ПОИСК И ЗАМЕНА

coun = text.count('l')  # Считает количество непересекающихся вхождений подстроки в исходную строку. Возвращает int
print(f'text.count("l") = {coun}')  # результат = 2

swi = text.startswith('he')  # Определяет начинается ли исходная строка заданной подстрокой. Возвращает True/False
print(f'text.startswith(\'he\') = {swi}')  # результат = False (т.к. в начале строки пробелы)

endswi = text.endswith('ld!')  # Определяет оканчивается ли исходная строка заданной подстрокой. Возвращает True/False
print(f'text.endswith(\'ld!\') = {endswi}')  # результат = False (т.к. в конце строки пробелы)

find = text.find(
    'w')  # Находит индекс первого вхождения подстроки в исходной строке. Возвращет int или -1, если не найдено.
print(f'text.find(\'w\') = {find}')  # результат = 9

rfind = text.rfind('d')  # Аналогичен find(), НО ищет с конца строки.
print(f'text.rfind(\'d\') = {rfind}')  # результат = 13

index = text.index('l')  # Аналогичен find(), НО если  не найдено возвращает исключение ValueError: substring not found
print(f'text.index(\'l\') = {index}')  # результат = 6

rindex = text.rindex('R')  # Аналогичен index(), НО ищет с конца строки
print(f'text.rindex(\'R\') = {rindex}')  # результат = 11

strip = text.strip()  # Возвращает копию строки у которой удалены пробелы в начале и в конце строки.
print(f'text.strip() = {strip}')  # результат = heLlo woRld!***

lstrip = text.lstrip()  # Возвращает копию строки у которой удалены пробелы в начале строки.
print(f'text.lstrip() = {lstrip}')  # результат = heLlo woRld!***

rstrip = text.rstrip()  # Возвращает копию строки у которой удалены пробелы в конце строки.
print(f'text.rstrip() = {rstrip}')  # результат =    heLlo woRld!***

del_strip = text.rstrip(
    '*')  # strip(), lstrip(), rstrip() могут принимать опциональный аргумент <chars>, который определяет набор символов для удаления.
print(f'text.rstrip(\'*\') = {del_strip}')  # результат =    heLlo woRld!

replace = text.replace('l', 'L')  # Возвращает копию строки со всеми вхождениями строки <old> замененными на <new>.
print(f'text.replace(\'l\', \'L\') = {replace}')  # результат =    heLLo woRLd!***

#                           КЛАССИФИКАЦИЯ СИМВОЛОВ

alnum = text.isalnum()  # Определяет состоит ли строка из буквенно-цифровых символов. Возвращает True/False
print(f'text.isalnum() = {alnum}')  # результат = False

alpha = text.isalpha()  # Определяет состоит ли строка из только буквенных символов. Возвращает True/False
print(f'text.isalpha() = {alpha}')  # результат = False

digit = text.isdigit()  # Определяет состоит ли строка из только из цифровых символов. Возвращает True/False
print(f'text.isdigit() = {digit}')  # результат = False

lower = text.islower()  # Определяет состоит ли строка только из символов нижнего регистра. Возвращает True/False
print(f'text.islower() = {lower}')  # результат = False

upper = text.isupper()  # Определяет состоит ли строка только из символов верхнего регистра. Возвращает True/False
print(f'text.isupper() = {upper}')  # результат = False

space = text.isspace()  # Определяет состоит ли строка только из символов пробела. Возвращает True/False
print(f'text.isspace() = {space}')  # результат = False

#                           ЮНИКОД

inord = ord('a')  # Позволяет определить код символа в таблице Unicode. Аргументом является char. Возвращает int.
print(f'ord(\'a\') = {inord}')  # результат = 97

inchr = chr(65)  # Позволяет по коду символа определить сам символ. Аргументом является int. Возвращает char.
print(f'chr(65) = {inchr}')  # результат = A
