#-*- coding:utf-8 -*-

import time
import os

#判断用户名和密码是否正确，接收 "用户名" 和 "密码" 返回 "True" 或者 "False"
def isAdministor(user_name, user_password):
    Administors = {'hon': 'hon233', 'bin': '181360226'}
    if user_name in Administors and Administors[user_name] in [user_password]:
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
    full_data = list()
    with open('data')  as f:
        for l in f:
            full_data.append(l[:-1].split())
    return full_data

#接收一个二维列表，将所有人员信息存入 "data" 文件
def SaveData(changed_data):
    with open('data', 'w') as f:
        for p in changed_data:
            l = ' '.join(p) + '\n'
            f.writelines(l)

#解决时间格式化的小时数错乱问题
def HourSwitch(h):
    h = int(h.lstrip('0')) + 8
    if h >= 24:
        h -= 24
    h = str(h)
    if int(h) < 10:
        h = '0' + h
    return str(h)

#备份以及初始化
def BackupAndInit(is_only_init):
    init_data = GetData()

    if not is_only_init:
        stamp_time = time.strftime('%Y%m%d%H%M%S', time.gmtime())
        os.system('cp data data_folder/' + stamp_time[:8] + HourSwitch(stamp_time[8:10]) + stamp_time[10:])
        os.system('cp personal_data data_folder/pd' + stamp_time[:8] + HourSwitch(stamp_time[8:10]) + stamp_time[10:] + ' -r')
        os.system('cp signed_data data_folder/sd' + stamp_time[:8] + HourSwitch(stamp_time[8:10]) + stamp_time[10:] + ' -r')
        if os.listdir('signed_data/'):
            os.system('rm signed_data/*')
        #找出最低分
        min_score = 23333
        for i in range(1, len(init_data)):
            min_score = min(min_score, int(init_data[i][6]))
        for i in range(1, len(init_data)):
            if int(init_data[i][6]) == min_score:
                init_data[i][2] = str(int(init_data[i][2]) - 5)
            if int(init_data[i][5]) > 9:
                init_data[i][2] = str(int(init_data[i][2]) + 5)

    if is_only_init:
        for i in range(1, len(init_data)):
            init_data[i][2] = '90'

    for i in range(1, len(init_data)):
        pfn = str(i)
        if i < 10:
            pfn = '0' + pfn
        os.system('cp personal_data/00 personal_data/' + pfn)
        init_data[i][3] = init_data[i][4] = init_data[i][5] = '0'
        init_data[i][6] = init_data[i][2]
    SaveData(init_data)


#接收一个整数，表示显示信息模式
"""
1 - 按剩余分数从小到大显示所有成员信息
2 - 按序号从小到大显示所有成员信息
3 - 只显示序号和姓名
4 - 显示单个人员具体信息
"""
def ShowInformation(show_mode):
    show_data = GetData()[1:]

    if show_mode in [1, 2]:
        if show_mode == 1:
            #按照二位列表的第 6 位元素（剩余积分）排序
            out_info = sorted(show_data, key = lambda x:x[-1])
            show_all_type = '按积分排名'
        else:
            out_info = show_data
            show_all_type = '按序号排名'
        print(show_all_type.center(100, '-'))
        print('序号\t\t姓名\t\t积分上限\t本月加分\t本月减分\t饱和分数\t剩余积分')
        for l in out_info:
            for w in l:
                print(w, end = '\t\t')
            print()
        print()

    elif show_mode == 3:
        line_num = 1
        for p in show_data:
            print(p[0] + ' ' + p[1], end = '\t\t')
            if line_num == 5:
                print()
                line_num = 0
            line_num += 1
        print()

    elif show_mode == 4:
        the_man = IsManExist(input('输入你想找的人名:'))
        if the_man:
            with open('personal_data/' + the_man[0]) as pf:
                this_reason = pf.readline().split()
                this_score = pf.readline().split()
                for i in range(len(this_reason)):
                    print(this_reason[i].ljust(10) + this_score[i])

#判断要找的人是否存在，存在则返回序号，不存在则返回空字符串
def IsManExist(find_str):
    find_data = GetData()[1:]
    for p in find_data:
        if find_str in p:
            return [p[0], p[1]]
    print('查无此人')
    return []

#接收序号判断该序号是否已经签到，若已签到，返回 "False"
def SingIn(who_sign):
    time_stamp = time.strftime('%Y%m%d', time.gmtime())

    if time_stamp not in os.listdir('signed_data/'):
        os.system('touch signed_data/' + time_stamp)

    with open('signed_data/' + time_stamp) as f:
        had_signed = f.readline().split()
    if who_sign in had_signed:
        return False
    had_signed.append(who_sign)
    with open('signed_data/' + time_stamp, 'w') as f:
        f.writelines(' '.join(had_signed))
    return True

#接收一个整数、一个人员序号的字符串，和一个分数变动原因
def ScoreOperation(score, operate_who, reason):
    #获取成员信息列表
    data = GetData()
    #读取成员位置
    step = int(operate_who[0])

    ####加减分记录####
    if score > 0:
        add_minus_pot = 3
    else:
        add_minus_pot = 4
        data[step][5] = '0'
    data[step][add_minus_pot] = str(int(data[step][add_minus_pot]) + score)
    ##################

    new_score = int(data[step][6]) + score

    ########处理分数越界########
    if new_score < 0:
        new_score = 0
    elif new_score > int(data[step][2]):
        ####处理分数饱和####
        over_score = new_score - int(data[step][2])
        data[step][5] = str(int(data[step][5]) + over_score)
        ####################
        new_score = int(data[step][2])
    ############################
    data[step][6] = str(new_score)

    #最后对数据进行保存
    SaveData(data)
    with open('personal_data/' + data[step][0]) as psf:
        reason_data = psf.readline().split()
        score_data = psf.readline().split()
    reason_data.append(reason)
    score_data.append(str(score))
    with open('personal_data/' + data[step][0], 'w') as psf:
        psf.writelines(' '.join(reason_data) + '\n')
        psf.writelines(' '.join(score_data) + '\n')

