# 输入数字计算阶乘
num = int(input('输入一个数字'))
res = 1
if num>1:
    for i in range(1,num+1):
        res *= i
    print(res)
else:
    print(num)

# 判断101到200之间有多少个素数并输出
for i in range(101,201):
    count = 0
    half = int(i/2)
    for j in range(2,half):
        # 从2开始逐个找i的因数（1和它本身可以忽略）（查找过程截止到i的一半即可），如果发现有因数，count加1，本次循环可以停止
        if i%j == 0:
            count += 1
            break
    # 循环结束后如果count没有改变（没有找到因数），即可判断为质数
    if count == 0:
        print(i)

# 将一个列表的数据赋值到另一个列表中，并反向输出
list = ['djfg',432,23,'fg9fd',109,'cvib']
# 声明一个新数组
colist = []
# print(type(len(list)))
for i in range(len(list)):
    j = len(list)-i-1
    # print(list[j])
    # 把已定义列表中的元素倒序添加到新数组中
    colist.append(list[j])
print(colist)

# 2
# 输入数字计算阶乘
num = int(input('输入数字'))
res = 1
if num>1:
    for i in range(1,num+1):
        res *= num
    print(res)
else:
    print(1)

# 判断101到200之间有多少个素数,并输出
for i in range(101,201):
    count = 0
    half = int(i/2)
    for j in range(2,half):
        if i % j == 0:
            count += 1
            break
    if count == 0:
        print(i)

# 将一个列表的数据复制到另一个列表中，并反向排序输出
list = ['gas',432,'hello','hi',89]
colist = []
for i in range(len(list)):
    j = len(list) - i - 1
    colist.append(list[j])
print(colist)

# 3
# 输入数字计算阶乘
num = int(input('输入一个数字'))
res = 1
if num>1:
    for i in range(1,num+1):
        res *= 1
    print(res)
else:
    print(1)

# 判断101到200之间有多少个素数并输出
for i in range(101,201):
    count = 0
    half = int(i/2)
    for j in range(2,half+1):
        if i%j == 0:
            count += 1
            break
    if count == 0:
        print(i)

# 将一个列表的数据复制到另一个列表中，并反向排序输出
list = ['hello',12,'world']
colist = []
for i in range(len(list)):
    j = len(list) - i - 1
    colist.append(list[j])
print(colist)