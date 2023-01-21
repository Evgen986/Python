def del_some_words(input):
    input_l = list(filter(lambda x: 'абв' not in x, input))
    print(input_l)
    return ' '.join(input_l)


with open("input.txt", encoding='UTF-8') as input_file:
    test = [word.split() for word in input_file.readlines()]
    print(f'после считывания {test}')
    test = test[0] + test[1]
    print(f'перед поп {test}')
    test = del_some_words(test)
    print(test)

