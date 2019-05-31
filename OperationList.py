#-*- coding:utf-8 -*-

def OperationalList(isAdministor):
    print('ACM实验室人员考勤系统'.center(80, '-'))
    print()
    print('\t- 按积分显示\t\t - 操作编号"1"\t\t - 操作命令"DisplayByIntegral"/"dbi"')
    print('\t- 按序号显示\t\t - 操作编号"2"\t\t - 操作命令"DisplayBySerialNumber"/"dbsn"')
    print('\t- 显示某个人员信息\t - 操作编号"3"\t\t - 操作命令"ShowOneInformation"/"soi"')
    if isAdministor:
        print('\t- 分数变动登记\t\t - 操作编号"4"\t\t - 操作命令"ScoreChangeRegistration"/"scr"')
        print('\t- 月末结算\t\t - 操作编号"5"\t\t - 操作命令"MonthlySettlement"/"ms"')
    else:
        print('\t- 进入管理员权限\t - 操作编号"4"\t\t - 操作命令"EnterAdministratorJurisdiction"/"eaj"')
        print('\t- 签到\t\t\t - 操作编号"5"\t\t - 操作命令"SignIn"/"si"')
    print('\t- 返回主界面\t\t - 操作编号"0"\t\t - 操作命令"Quit"/"q"')

def ScoreOperationalList():
    print('积分变动可用操作列表'.center(80, '-'))
    print('加分项:')
    print('\t- ' + '练习赛榜单前五[5]\t - 操作编号"a1"\t\t - 操作命令"TopFiveList"/"tfl"')
    print('\t- ' + '练习赛榜单六到十[3]\t - 操作编号"a2"\t\t - 操作命令"ListsSixToTen"/"lstt"')
    print('\t- ' + '重要比赛得奖[20]\t - 操作编号"a3"\t\t - 操作命令"ImportentMatchGetPrize"/"imgp"')
    print('\t- ' + '讲知识[10]\t\t - 操作编号"a4"\t\t - 操作命令“TeachKnowledge”/"tk"')
    print('\t- ' + '做题解[2]\t\t - 操作编号"a5"\t\t - 操作命令"MakeQuestionSolution"/"mqs"')
    print('减分项:')
    print('\t- ' + '请假[10]\t\t - 操作编号"m1"\t\t - 操作命令"AskForLeave"/"afl"')
    print('\t- ' + '无故缺勤[30]\t\t - 操作编号"m2"\t\t - 操作命令"AbsenceFromDuty"/"afd"')
    print('\t- ' + '无故迟到/早退[15]\t - 操作编号"m3"\t\t - 操作命令"LateOrLeaveEarly"/"lale"')
    print('\t- ' + '比赛不写[18]\t\t - 操作编号"m4"\t\t - 操作命令“MatchNotWrite”/"mnw"')
    print('\t- ' + '玩游戏[90]\t\t - 操作编号"m5"\t\t - 操作命令“PlayGameInLab”/"pgil"')
    print('\t- ' + '穿拖鞋[3]\t\t - 操作编号"m6"\t\t - 操作命令"InSlippers"/"is"')
    print('\t- ' + '没有及时完成任务[20]\t - 操作编号"m7"\t\t - 操作命令"MissionNotOnTime"/"mnot"')
    print('\n\t- ' + '其他分数变动操作\t - 操作编号"8"\t\t - 操作命令"OtherSatuation"/"os"')
    print('\n\t- ' + '返回上一界面\t\t - 操作编号"0"\t\t - 操作命令"Quit"/"q"')

