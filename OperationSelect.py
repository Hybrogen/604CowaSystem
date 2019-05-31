#-*- coding:utf-8 -*-

import os
import Operations
import OperationList

def BasicOperation(operation, is_administor):
    if operation in ['1', 'DisplayByIntegral', 'dbi']:
        Operations.ShowInformation(1)
    elif operation in ['2', 'DisplayBySerialNumber', 'dbsn']:
        Operations.ShowInformation(2)
    elif operation in ['3', 'ShowOnceInformation', 'soi']:
        Operations.ShowInformation(4)

    #########################管理员特殊操作#########################
    elif is_administor:
        if operation in ['4', 'ScoreChangeRegistration', 'scr']:

            scores = {'a1': 5, 'a2': 3, 'a3': 20, 'a4': 10, 'a5': 2, 'm1': -10, 'm2': -30, 'm3': -15, 'm4': -18, 'm5': -90, 'm6': -3, 'm7': -20}
            reasons = { 'a1': '练习赛前五', 'a2': '练习赛前十', 'a3': '大型比赛得奖', 'a4': '知识讲解', 'a5': '做题解\t', 
                        'm1': '请假\t', 'm2': '无故缺勤', 'm3': '无故迟到/早退', 'm4': '比赛不写', 'm5': '玩游戏\t', 
                        'm6': '穿拖鞋\t', 'm7': '没有及时完成任务'}

            ####循环之前首先输入一次信息####
            Operations.ShowInformation(3)
            OperationList.ScoreOperationalList()
            informations = input('请输入 <操作> 和 <成员[编号/姓名]> [空格隔开]:').split()
            if len(informations) != 2:
                informations.append('00')
            (score_operation, operate_who) = informations
            operate_who = Operations.IsManExist(operate_who)
            ################################

            while score_operation not in ['0', 'Quit', 'q']:
                if operate_who:
                    if score_operation in ['8', 'OtherSatuation', 'os']:
                        operate_score, operate_reason = input('输入要变动的分数和原因[空格隔开]:').split()
                        operate_score = int(operate_score)
                    else:
                        operate_score = scores[score_operation]
                        operate_reason = reasons[score_operation]
                    Operations.ScoreOperation(operate_score, operate_who, operate_reason)
                #在循环末端输入信息，便于判断退出条件
                Operations.ShowInformation(3)
                OperationList.ScoreOperationalList()
                informations = input('请输入 <操作> 和 <成员[编号/姓名]> [空格隔开]:').split()
                if len(informations) != 2:
                    informations.append('00')
                (score_operation, operate_who) = informations
                operate_who = Operations.IsManExist(operate_who)
        elif operation in ['5', 'MonthlySettlement', 'ms']:
            Operations.BackupAndInit(is_only_init = False)
        elif operation in ['INITIALIZATION']:
            Operations.BackupAndInit(is_only_init = True)


    ################################################################

    elif operation in ['5', 'SignIn', 'si']:
        who_sign_in = Operations.IsManExist(input('输入您的 序号/姓名 进行签到:'))
        if who_sign_in:
            if Operations.SingIn(who_sign_in[0]):
                input('{} 签到成功\n'.format(who_sign_in[1]))
            else:
                input('{} 今天已完成签到，无法多次签到'.format(who_sign_in[1]))

