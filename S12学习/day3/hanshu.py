# /usr/bin/env python
# coding=utf-8


# 函数
# def 是关键字，下面的都是函数
# def mail()  函数名(參數）
#         參數

def mail():
    n = 123
    n += 1
    print(n)
    return n


# mail()
# 执行函数 mail(),mail是函数名
# 函数名赋值。 f指向函数名，f加（）也是调用这个函数
# f = mail
# f()

ret = mail()
print(ret)
# 函數的返回值,用return n
# 接收返回值，赋值给变量
# return后面跟什么就会返回什么,如果没有return返回值就是None
'''
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def mail():
    ret = True
    try:
        msg = MIMEText('使用python發送郵件，非常方便！！！', 'plain', 'utf-8')
        msg['from'] = formataddr(['smile', 'shen_wandong@163.com'])
        msg['To'] = formataddr(['Hello', '844843463@qq.com'])
        msg['Subject'] = "Email"

        server = smtplib.SMTP("smtp.163.com", 25)
        server.login("shen_wandong@163.com", "*****")
        server.sendmail("shen_wandong@163.com", ['844843463@qq.com', ], msg.as_string())
        server.quit()
    except Exception:
        ret = False
    return ret


ret = mail()
if ret:
    print("發送成功")
else:
    print("發送失敗")
    '''


# return会终结函数的执行
def show():
    print('a')
    if 1 == 1:
        return [11, 22]
    print('b')


s = show()

# 函数参数
# 加了参数的函数执行的时候也需要加参数
# 形参需要实参
# def mail(user):  形参
#     server.sendmail([user,],)  这里就可以调用这个参数
# ret = mail('80470335@qq.com') 实参
'''
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def mail(user):
    ret = True
    try:
        msg = MIMEText('使用python發送郵件，非常方便！！！', 'plain', 'utf-8')
        msg['from'] = formataddr(['smile', 'shen_wandong@163.com'])
        msg['To'] = formataddr(['Hello', '844843463@qq.com'])
        msg['Subject'] = "Email"

        server = smtplib.SMTP("smtp.163.com", 25)
        server.login("shen_wandong@163.com", "jeiidde520")
        server.sendmail("shen_wandong@163.com", [user, ], msg.as_string())
        server.quit()
    except Exception:
        ret = False
    return ret


ret = mail('80470335@qq.com')
ret = mail('844843463@qq.com')
ret = mail("shen_wandong@163.com")
if ret:
    print("發送成功")
else:
    print("發送失敗")
'''


# 无参数 show():
# 有参数
def how(arg):
    print(arg)


how('shisonghao')


# 两个参数..多个参数
def show(arg, xxx):
    print(arg, xxx)


show('salala', '888')


# 默认参数 默认参数可以赋值，也可以传参数，默认参数也可以有多个
# 默认参数一定要放在最后面
def na(a1, a2=999):
    print(a1, a2)


na('神话', 1233)


# 指定参数，在传参数时，指定参数，
def pa(m1, m2):
    print(m1, m2)


pa(m2='susu', m1='88@qq.com')


# 动态参数
def shen(arg):
    print(arg)


# 等于n就是一个列表，n传给函数arg参数
n = [11, 22, 33, 44]
shen(n)


# 带一个*接收参数为元组，所有参数为一个元组
def dong(*arg):
    print(arg, type(arg))


dong(11, 22, 33, 44, 55)


# 参数带两个**，表示接收的参数为字典，传如参数格式和原来是不一样的
def wan(**arg):
    print(arg, type(arg))


# 传入字典参数
wan(a=223, b=33, c=23, d=13, e=1231, f=312, g=13, h=1)


# 多个参数联合
# 一个*的放前面，两个**的必须放在后面


def make(*args, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs))


# 传入的参数会自动在元组和字典中
# make(11, 22, 33, ml='kk', mp='ko')
# 另一种传参数的方式
li = [12, 23, 234, 454, 23, 66]
di = {'name': 'shenwd', 'age': 28, 'gender': 'man'}
# 变量传入动态参数时，需要对传入的实参参数加*
make(*li, **di)

# format使用,格式化传入参数，传入列表的方法
s1 = "{0} is {1}"
l =['alex','sb']
p2 = s1.format(*l)
print(p2)

# 传入字典的方法,使用两个*
s2 = "{name},{message}"
li = {'name':'alex', 'message':'welcome to space'}
# li = s2.format(name='alex', message='welcome to space')
# 另一种方法
result = s2.format(**li)
print(li)

# lambda 表达式是简单函数的表示方式
# 定义一个函数,一个函数a，给a传入参数99,相加
# 首先定义函数需要lambda，冒号前面是函数，冒号后面是函数体
# 创建了形式参数a，创建了函数内容a+1,并把结果return
func = lambda a: a + 1
ret = func(99)
print(ret)


# 内置函数
# abs()
# all() 如果传入的序列所有的值都是真的，才是True
# all([1,2,3,4]) 是真的
# 空字符串是假的，None是假的，所有空的都是假的
# any() 如果有一个是真的，那就是真的
# any(['',[],{},None,1])
# ascii() 这个函数和repr()函数一样，返回一个可打印的对象字符串方式表示
# bin(10)返回二进制 ）0B就表示二进制
# bytearray()转换成字节数，汉字一个是三个字节
# p =bytearray("史松浩",encoding='utf-8')
# print(p)
# bytes()转换成字节
# p = bytes('史松浩',encoding='utf-8')
# print(p)
# callable()函数是否可执行 ，返回布尔值
# print(ord('a'))
# ord() 把字符串转换成ascii码
# chr() 把数字转换成ascii码
# import random 生成随机数
# print(random.random())
# 生成随机数
# random.randint(1,99)
# compile()编译使用
# complex() 复数
# delattr()反射
# dir() 返回当前参数的属性，方法列表
# divmod() 返回的是a//b（除法取整）以及a对b的余数
# enumerate()，从1开始序列
# 这个1代表初始值是1
# al = ['alex','eirc','lily']
# for i,item in enumerate(al,1):
#     print(i,item)
# print(eval("6*8"))  将字符串str当成有效的表达式来求值并返回计算结果
# exec()编译代码

#################################
# filter() 对于序列中的元素进行筛选，最终获取符合条件的序列
# st = ['a','b','c','d']
# def fun(s):return s if s != 'a' else None
# ret = filter(fun,st) 第一个参数是一个函数，会循环第二个函数
# for i in ret:print(i)  只有遍历才能取到每个值
# 第二种写法
# 函数的返回值只有是True的时候才返回,filter过滤的作用
st = [11,33,44,55]
def func(x):
    if x>33:
        return True
    else:
        return False
m = filter(func,st)
print(list(m))

##################################
# map() 遍历序列，对序列中每个元素进行操作，最终获取新的序列
# li = [11,22,33]
# s1 = [1,2,3]
# new_list = map(lambda a,b:a+b,li,s1)  map第一个参数是一个函数，map的两个参数会循环后面的两个参数
# # for i in new_list:print(i)  第一种输出方式
# l = list(new_list) 第二种输出方式
# print(l)
#################################
# 使用函数写法
# li = [11,22,33]
# def func(x):
#     return x+100
# new_li = map(func,li) 第一个参数也是函数,第二个参数是变量参数
# print(list(new_li)) 打印一个list

# format 格式化
# frozenset() 不能修改的集合
# globals()当前的所有变量

# hash()哈希值,返回对象的哈希值,哈希值是使用一个整数表示,通常使用在字典里,以便实现快速查询键值.
# li = 'abc'
# print(hash(li))

# help()查看对象属性方法
# print(help(hex))

# hex()转换一个整数对象为十六进制的字符串表示,比如0x的格式,如果对象不是一个整数,应定义一个方法__index__()返回整数
# 如果想把本函数的结果转换为整数类型,需要int()函数,并且使用基数为16的方式转换,浮点数转换为十六进制需要float.hex()来转换
# a = 'ad'
# print(hex(a)) 输出一个十六进制 0x7b
# print(hex(int(a)))

# id查看对象在内存中的id

# input  键盘输入
# int 整形
# len 对象的长度
# list 列表
# locals() 局部变量

# max() 最大值
# a =(11,22,33)
# print(max(a))
# min(11,22,33)最小值


# next()
def h():
    print('Wen')
    yield 5
    print('Fighting')
c = h()
c.__next__()
