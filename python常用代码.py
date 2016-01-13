# coding=utf-8


# 生成随机数random函数
import random  # 引入模块

rnd = random.randint(1, 100)  # 生成1-100之间的随机数
print rnd

# 读文件
f = open(r"README.md", "r")
lines = f.readlines()  # 读取全部文件
for line in lines:
    print line
# 写文件
f = open("README.md", "r+")  # 可读可写模式
f.write("Hello")


# 装饰器的使用
def decofun(fun):
    def _mydeco(*args, **kwargs):
        print('before fun!')

        ret = fun(*args, **kwargs)

        print('after fun', ret)

        return ret

    return _mydeco  # 新的函数，用于替换原有标示符


@decofun
def funtest():  # funtest被替换为decofun

    print('now in funtest!')

    return 1


funtest()
