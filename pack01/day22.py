# 输入数字计算阶乘
num = int(input('输入一个数字'))
res = 1
if num>1:
    for i in range(1,num+1):
        res *= i
    print(res)
else:
    print(num)

# 判断101-200之间有多少个素数，并输出
# for i in range(101,201):
#     for j in range(2,i+1):
#         if i%j == 0:
#             continue


# 将一个列表的数据复制到另一个列表中，并反向排序输出
list = ['djfg',432,23,'fg9fd',109,'cvib']
colist = []
for i in range(len(list)):
    # print(i)
    j = len(list)-i-1
    print(j)
    colist[j] = list[i]
print(colist)

