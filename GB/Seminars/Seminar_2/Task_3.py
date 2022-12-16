# 3. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

text_1 = input('Введите текст: ')
text_2 = input('Введите текст: ') 
count = text_1.lower().count(text_2.lower()) 
print(f'Количество вхожднений = {count}')

#       Решение Николая
# str_1 = 'sdfsdfsdfxcgvhdfghsdfgsdhdfghdfghdsfgdfbs' 
# str_2 = 'sdf'

# counter = 0
# for i in range(len(str_1) - len(str_2)):
#     flag = False
#     if str_2[0] == str_1[i]:
#         flag = True
#         for j in range(1,len(str_2)):
#             if str_2[j] != str_1[i + j]:
#                 flag = False
#         if flag:
#             counter += 1
            
# print(f'Вторая строка встречается в первой {counter} раз')
