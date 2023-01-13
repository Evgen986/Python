def coding(text: str, step):
    lower_alph = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for el in text:
        if not el.isalpha():
            result += el
        else:
            result += lower_alph[(lower_alph.find(el.lower()) + step) % len(lower_alph)]
    for index in range(len(text)):
        if text[index].isupper():
            result = result[:index] + result[index].upper() + result[index + 1:]
    return result


text = input().split()
code_text = ''
print(len(text[0]))
for element in text:
    count = 0
    for e in element:
        if e.isalpha():
            count += 1
    code_text += coding(element, count) + ' '
print(code_text.rstrip())
