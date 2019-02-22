import random
list = []
for i in range(20):
    num = random.choice(range(100))
    # print(num)
    list.append(num)
# print(list)
list[::2] = sorted(list[::2],reverse=True)
print(list)

