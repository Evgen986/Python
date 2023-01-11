#  g i v e t h h i i s m a a a n a g u u n
text = input().replace(' ', '')
count = int(input())
result_list = list()
while len(text) != 0:
    new_list = list()
    if count > len(text):
        count = len(text)
    for index in range(count):
        new_list.append(text[index])
    text = text[count:]
    result_list.append(new_list)
print(result_list)
