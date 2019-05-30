#-*- coding:utf-8 -*-

#判断用户名和密码是否正确，接收 "用户名" 和 "密码" 返回 "True" 或者 "False"
def isAdministor(user_name, user_password):
    Administors = {'hon': 'hon233', 'bin': '181360226'}
    if Administors[user_name] in [user_password]:
        return True
    return False

#管理员登录，如果不是管理员返回 "3" ，如果是返回0,1,2
def AdministorEnter():
    for i in range(3):
        user_name = input('输入用户名:')
        user_password = input('输入密码:')
        if isAdministor(user_name, user_password):
            break
        else:
            print('用户名或密码错误，请重新', end = '')
            i += 1
    return i

#返回一个二维列表，包含所有信息
def GetData():
    Data = list()
    with open('.data')  as f:
        for l in f:
            Data.append(l[:-1].split())
    return Data

#接收一个二维列表，将所有人员信息存入 "data" 文件
def SaveData(Data):
    with open('.data', 'w') as f:
    f.writelines('序号 姓名 积分上限 本月加分 本月减分 饱和分数 剩余积分\n')
    for p in Data:
        l = ' '.join(p) + '\n'
        f.writelines(l)

#接收一个整数，表示显示信息模式
"""
1 - 按剩余分数从小到大显示所有成员信息
2 - 按序号从小到大显示所有成员信息
3 - 只显示序号和姓名
4 - 显示单个人员具体信息
"""
def ShowInformation(show_mode):
    show_data = GetData()
    del data[0]
    if show_mode in [1, 2]:
        if show_mode == 1:
            #按照二位列表的第 6 位元素（剩余积分）排序
            out_info = sorted(data, key = lambda x:x[-1])
        else:
            out_info = data
        print('序号\t\t姓名\t\t积分上限\t本月加分\t本月减分\t饱和分数\t剩余积分')
        for l in out_info:
            for w in l:
                print(w, end = '\t\t')
            print()
        print()
    elif show_mode == 3:
        line_num = 1
        for p in data:
            print(p[0] + ' ' + p[1], end = '\t\t')
            if line_num == 5:
                print()
                line_num = 0
            line_num += 1
        print()
    elif show_mode == 4:
        the_man = IsManExist(input('输入你想找的人名:'))
        if the_man:
            with open('personal-data-' + the_man[0]) as pf:
                for l in pf:
                    print(l)

#判断要找的人是否存在，存在则返回序号，不存在则返回空字符串
def IsManExist(find_str):
    find_data = GetData()
    for p in find_data:
        if find_str in p:
            return p[0]
    print('查无此人')
    return ''

#接收序号判断该序号是否已经签到，若已签到，返回 "False"
def SingIn(who_sign):
    time_stamp = time.strftime('%Y%m%d', time.gmtime())
    with open(time_stamp + 'signed') as f:
        had_signed = f.readline().split()
    if who_sign in had_signed:
        return False
    had_signed.append(who_sign)
    with open(time_stamp + 'signed', 'w') as f:
        f.writeline(' '.join(had_signed))
    return True
