def get_sum(a,b):
    if a == b: return a
    else:
        c = 0
        if(a<b):
            for i in range(a, b+1):
                c+=i
            return c
        else:
            for i in range(b, a+1):
                c+=i
            return c

a = 1
b = 100
print(get_sum(a,b))
