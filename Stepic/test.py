import math

n = math.log2(float(input()))
index = str(n).find('.')
if int(str(n)[index + 1:]) != 0:
    n = int(n) + 1
print(int(n))
