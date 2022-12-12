def is_isogram(string):
    string = string.lower()
    for i in range(0, len(string)):
        temp = string[i].lower()
        for j in range(i+1, len(string)):
            if temp == string[j]:
                return False
    return True

text = 'moOse'
print(is_isogram(text))