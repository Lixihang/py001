import random
str = ''
str0 = 'qwertyuiopadfghjklzxcvbnm'
for i in range(1000):
    str += random.choice(str0)
# print(str)
# print(len(str))
dict = {}
for i in str:
    key = dict.get(i)
    if key == None:
        dict[i] = 1
    else:
        dict[i] += 1
print(dict)