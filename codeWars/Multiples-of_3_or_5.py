def solution(number):
    # if number == 0:
    #     return 0
    # else:
        sum = 0
        for i in range(3, number):
            if i%5 == 0 or i%3 == 0:
                sum += i
                print(f'i={i}, sum={sum}')
        return sum

num = 200
print(solution(num))