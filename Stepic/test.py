for i in range(40):
    num = i
    print(num, ' ', end='')
    if -1<num<37:
        if num==0:
            print('зеленый')
        elif 0<num<11 or 18<num<29:
            if num%2!=0:
                print('красный')
            else:
                print('черный')
        else:
            if num%2!=0:
                print('черный')
            else:
                print('красный')
    else:
        print('ошибка ввода')