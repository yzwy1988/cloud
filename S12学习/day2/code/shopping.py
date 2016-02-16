# -*-coding:utf-8-*-
# author:shen
# DATE:2016/1/27
import sys
import getpass

# user_account = open('user_account', 'r')
# for user in user_account.readlines():

# 条件是否为true，进入此循环
count = 0
while count <3 :
    # 输入用户名
    input_user = input("Please input your user:")
    # input_passwd = str(input(r"请输入你的密码："))
    user_account = open('user_account.db', 'r')
    # user_list = user_account.readlines()
    for user_line in user_account.readlines():
        user = str(user_line).strip().split()[0]
        # str(user_line).split()[0] == input_user
        # user = str(user_line).split()
        # input_user == user_line.split()[0] and input_passwd == user_line.split()[1]
        #     print("欢迎光临")
        #     break
        # else:
        #     print(r"用户名或密码错误，请重新输入")
        #     continue
        while input_user == user:
            input_passwd = input('请输入密码')
            passwd = user_line.strip('\n').split()[1]
            if input_passwd == passwd:
                print(r"欢迎登录购物系统")
                goods = open('goods', 'r')
                for item in goods.readlines():
                        print(item.split()[0])  #.strip(''))
                    # for k, v in goods.readlines():
                    #     print('%s,%s' % (k, v))
            else:
                print(r'用户名错误，请重新输入！')

    else:
        print(r'用户名错误，请重新输入！')
        continue
    count += 1
    user_account.close()
