def square_digits(num):
    text = str(num)
    sqr_text = ''
    for i in text:
        sqr_text += str(int(i)**2)
    return int(sqr_text)

num = 9119
print(square_digits(num))