# Формат входных данных
# В первой строке дается число n 1≤ n ≤ 25 – сдвиг,
# во второй строке даётся закодированное сообщение в виде строки со строчными латинскими буквами.
#
# Формат выходных данных
# Программа должна вывести одну строку – декодированное сообщение.
# Обратите внимание, что нужно декодировать сообщение, а не закодировать

num = int(input())
text = input()
decoder = ''
for symbol in text:
    index = ord(symbol)
    count = num
    while count != 0:
        if index == 96:
            index = 122
        index -= 1
        count -= 1
    decoder += chr(index)
print(decoder)
print(ord('f'))