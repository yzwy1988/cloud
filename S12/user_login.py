# /usr/bin/env python
# -*-coding:utf-8-*-
# 编写登录接口：
# 1. 输入用户名密码
# 2. 认证成功后显示欢迎信息
# 3. 输错三次后锁定


# 定义用户名密码初始值
user = "zhangsan"
passwd = "888"

# login_count = 0

# 条件是否为true，进入此循环
while True:
    # 输入用户名
    input_user = input("Please input your user:")
    # 判断输入的用户名是否正确，如果不正确提示用户重新输入
    if input_user != user:
        print(r"帐户名不正确，请重新输入！")
        continue
    # for循环，密码输入3次
    for i in range(3):
        # 输入密码并判断输入的是否正确，不正确给出提示重新输入
        input_passwd = input("Please input your password:")
        if input_passwd != passwd:
            print(r"密码不正确请重新输入！")
            # login_count += 1
            # continue
        # 如果账户密码都正确给出提示
        else:
            print(r"欢迎你！登录成功")
            break
    # 如果输入三次密码都错误，账户锁定并退出
    else:
        print(r"用户被锁定")
        break
    break
