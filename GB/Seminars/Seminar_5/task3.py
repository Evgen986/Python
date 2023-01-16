# 38. Напишите программу, удаляющую из текста все слова, содержащие "абв".
text = 'пра прАБВ огнр длорпАБВовгв зщзыфшвщ вфыыАБВгыоы АБВывовдлыф'

# def delword(elem: str):
#     if 'абв' in elem.lower():
#         if not elem[-1].isalnum() and not elem[-1].isspace():
#             elem = elem.replace(elem[:-1], '')
#
#         else:
#             elem = elem.replace(elem, '')
#     return elem
#
#
# new_text = list(map(delword, text.split()))
# new_text = [el for el in new_text if len(el)]
# print(' '.join(new_text))

# test = 'вфыыАБВгыоы!'
# index = test.find(',' or '1')
# print(f'индекс {index}')
# print(f'буквы {"абв" in test.lower()}')
# print(f'знаки препинания: {test.rfind(",.!?") > 0}')
# temp = 'hfhfh'
# temp = temp.replace(temp, '')
# print(temp)

text = list(filter(lambda el: 'абв' not in el.lower(), text.split()))
print(' '.join(text))
