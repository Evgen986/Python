text = '1 2 3 5 8 15 23 38'
my_list = [(int(i), int(i)**2) for i in text.split() if int(i) % 2 == 0]
print(my_list)
