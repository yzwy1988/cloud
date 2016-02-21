# -*-coding:utf-8-*-
# author:shen
# DATE:2016/2/18


# 装时期(必备)
def login(func):
    def wrapper(*arg, **kwargs):
        ret = func(*arg, **kwargs)
        return ret

    return wrapper


def show():
    return 'show'


# show,show()是不一样的，show（）是找到函数执行函数，show是指向内存不执行
new_show = login(show)

# # 第一波
# def foo():
#     print("foo")
#
# foo  # 表示是函数
# foo()   # 表示执行foo函数
#
# # 第二波
# def foo():
#     print("foo")
#
# foo = lambda x: x + 1
# foo()   # 执行下面的lambda表达式,而不在是原来的foo函数,因为函数foo被重新定义了

# 非装饰器实现

'''
def login(func):
    print("passed user verification...")
    return func   # tv函数存放在内存中


def home(name):
    print("welcome [%s] to home page" %name)


def tv(name):
    print("welcome [%s] to tv page" %name)


def move(name):
    print("welcome [%s] to move page"%name)


tv = login(tv)
tv('Alex')  # 给tv传入参数
move = login(move)
move('Shen')
home = login(home)
home('baike')'''


# 执行login函数,tv会传给login(func),执行完return func,tv会放在内存中,在执行tv()函数,打印语句!

# 装饰器方法实现


def login(func):
    def inner(*args):
        print("passed user verification...")
        func(*args)  # func函数存放在内存中,*args,可以传入多个参数或者一个参数

    return inner


@login
# @函数就执行这句先调用login函数
# 给home传入多个参数,在fun(*args)添加*
def home(name, passwd):
    print("welcome [%s] to home page [%s]" % (name, passwd))


def tv(name):
    print("welcome [%s] to tv page" % name)


def move(name):
    print("welcome [%s] to move page" % name)


home("Yamaha", "Super")
