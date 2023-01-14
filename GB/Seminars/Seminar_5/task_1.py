with open('nums.txt', 'r') as data:
    nums_list = [int(el) for el in data.read().split()]
counter = nums_list[0]+1
print(nums_list)
for index in range(1, len(nums_list)):
    if counter != nums_list[index]:
        print(counter)
        break
    else:
        counter += 1
