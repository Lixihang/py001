import random
s = 'The column above illustrates apparently' \
    ' the polularity of people ' \
    'doing exercise in a certain year ' \
    'from 2013 to 2018.Based upon the data,' \
    'we can see that python is wonderful. ' \
    'python is wonderful. Python '
s = s.replace('.','')
# print(s)
s = s.split(' ')
# print(s)
# 删除最后一个元素（空格）
s.pop()
dict = {}
for i in s:
    key = dict.get(i)
    if key == None:
        dict[i] =1
    else:
        dict[i] += 1
dict1 = {}
gs = list(dict.values())
gs.sort()
# print(gs)
# 去重
gs = list(set(gs))
for i in gs:
    for j in dict:
        if dict[j] == i:
            dict1[j] = i
print(dict1)
