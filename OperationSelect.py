#-*- coding:utf-8 -*-

import os
import Operations
import OperationList

def BasicOperation(operation, is_administor):
    if operation in ['1', 'DisplayByIntegral', 'dbi']:
        os.system('clear')
        Operations.ShowInformation(1)
    elif operation in ['2', 'DisplayBySerialNumber', 'dbsn']:
        os.system('clear')
        Operations.ShowInformation(2)
    elif operation in ['3', 'ShowOnceInformation', 'soi']:
        os.system('clear')
        Operations.ShowInformation(4)

    #########################管理员特殊操作#########################
    elif is_administor:
        if operation in ['4', 'ScoreChangeRegistration', 'scr']:
            score_operation = ''
            while score_operation not in ['0', 'Quit', 'q']:
                os.system('clear')
                Operations.ShowInformation(3)
                operation_who = input('请输入想要修改分数记录的成员[编号/姓名]:')
                if Operations.IsManExist(operation_who):
                    while score_operation not in ['0', 'Quit', 'q']:
                        OperationList.ScoreOperationalList()
                        score_operation = input()
                else:
                    input('查无此人\n请按 ENTER 键继续')
                    continue
    ################################################################

    elif operation in ['5', 'SignIn', 'si']:
        os.system('clear')
        who_sign_in = Operations.IsManExist(input('输入您的 序号/姓名 进行签到:'))
        if who_sign_in:
            if Operations.SingIn(who_sign_in[0]):
                input('{} 签到成功\n'.format(who_sign_in[1]))
            else:
                input('{} 今天已完成签到，无法多次签到'.format(who_sign_in[1]))

    elif s in ['0', 'Quit', 'q']:			#0 - 退出用户界面
        IsCommand = False
        return 'Quit'
    elif IsCommand:
        if s in ['4', 'ScoreChangeRegistration', 'scr']:#4 - 考勤登记
            CheckWorkAttendance()
        elif s in ['5', 'MonthlyAccounting', 'ma']:	#5 - 月末结算
            MonthlyAccounting()
        elif s in ['6', 'BlackAdd', 'ba']:		#6 - 黑幕加分
