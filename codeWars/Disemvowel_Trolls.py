def disemvowel(string_):
    for i in 'a','e','i','o','u', 'A', 'E', 'I', 'O', 'U':
        string_ = string_.replace(i,'')
    return string_

text = 'This website is for losers LOL!'
text2 = disemvowel(text)
print(text2)