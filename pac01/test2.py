import random
list = []
list1 = []
list2 = []
for i in range(50):
    num = random.choice(range(-10,11))
    list.append(num)
    if num > 0:
        list1.append(num)
    elif num < 0:
        list2.append(num)
# print(list)
print(list1)
print(list2)
