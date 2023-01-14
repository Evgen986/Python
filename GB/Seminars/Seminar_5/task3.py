# 38. Напишите программу, удаляющую из текста все слова, содержащие "абв".
text = 'пра прАБВ огнр длорпАБВовгв зщзыфшвщ вфыыАБВгыоы АБВывовдлыф'

# def delword(elem:str):
#     if 'абв' in elem.lower():
#         elem = elem.replace(elem, '')
#     return elem

# temp = 'hfhfh'
# temp = temp.replace(temp, '')
# print(temp)

text = list(filter(lambda el: 'абв' not in el.lower(), text.split()))
print(' '.join(text))
