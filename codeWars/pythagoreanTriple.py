def pythagorean_triple(integers):
    integers.sort()
    if integers[0]**2 + integers[1]**2 == integers[2]**2:
        return True
    else:
        return False

list = [5,4,3]
print(pythagorean_triple(list))
