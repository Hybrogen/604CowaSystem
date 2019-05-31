#-*- coding:utf-8 -*-

import OperationList
import OperationSelect
import Operations
import os
import time

if __name__ == '__main__':
    quit_operation = ''
    while quit_operation not in ['000hon000']:
        is_administor = False

        Operations.ShowInformation(1)
        quit_operation = input('输入 [start] 进入操作:')

        #进入系统开始进行操作
        if quit_operation in ['start']:
            over_time = 0

            #开始时先进行一次选择
            OperationList.OperationalList(is_administor)
            operation = input('输入想要进行的操作:')
            while operation not in ['0', 'Quit', 'q']:
                if not is_administor and operation in ['4', 'EnterAdministratorJurisdiction', 'eaj']:
                    if over_time > time.time():
                        print('暂时无法登录，请 {} 分钟后重试...'.format(int((over_time - time.time())/60)))
                    elif Operations.AdministorEnter() == 3:
                        over_time = time.time() + 650
                        print('登录失败')
                    else:
                        is_administor = True
                        print('登录成功')
                else:
                    OperationSelect.BasicOperation(operation, is_administor)
                #在执行末端进行选择来确保 "Quit" 命令的运行
                OperationList.OperationalList(is_administor)
                operation = input('输入想要进行的操作:')

            #在退出到主界面后退出管理员用户
            is_administor = False


