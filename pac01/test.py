# 对手机号的号段进行判断
# 号段任意给出6个作为模拟号段即可.判断手机号码是否是由数字组成的
phone = input('输入手机号')
list = [182,183,159,138,137,133]
try:
    # 将输入内容转化为纯数字
    int(phone)
    if (len(phone) == 11):
        phonehead = int(phone[0:3])
        print(type(phonehead))
        flag = 'false'
        for i in list:
            if (phonehead == i):
                print('手机号正确')
                flag = 'true'
                break
        if flag == 'false':
            print('手机号不正确')
except ValueError:
    print('输入格式错误')