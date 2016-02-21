# /usr/bin/env python
# -*- coding:utf-8 -*-


# 迭代器
# 特点:
# 1.访问者不需要关心迭代器内部的结构,进需通过next()方法不断取下一个内容,
# 2.不能随机访问集合中的某个值,只能从头到尾依次访问
# 3.访问到一半时不能回退
# 4.便于循环比较大的数据集合,节省内存

# with open('test','r') as f:
#     a = f.readlines()
#     print(a)
#     pa = iter(a)
#     print(pa.__next__())
#
# # 用__next__取迭代器里的值,最后没有就报错了
# p = iter([1,2,3])
# print(p.__next__())
# print(p.__next__())
# print(p.__next__())

# 生成器
# 定义：一个函数调用时返回一个迭代器，那这个函数就叫做生成器（generator），如果函数中包含yield语法，那这个函数就会变成生成器
# 一个函数调用的时候返回一个迭代器,那这个函数就叫做生成器(generator)
# yield语法   yield后面的语句还会执行


# 调用函数时就要等着函数给返回值
# yield就是让程序可以中断
'''
def cash_out(amount):
    while amount > 0:
        amount -= 1
        yield 1
        print("擦，又来取钱了。败家仔！")
#传给函数实参 cash_out(5)
atm = cash_out(5)
print("取到钱%s万" % atm.__next__())
# 执行第一个print时,执行到函数中的yield后,返回执行下一个print,第二个执行时接着执行yield下面的print语句,执行完后在执行函数
print("花掉花掉！")
print("取到钱 %s 万" %atm.__next__())
print("取到钱 %s 万" %atm.__next__())
print("花掉花掉！")
print("取到钱 %s 万" %atm.__next__())
print("取到钱 %s 万" %atm.__next__())
print("取到钱 %s 万" %atm.__next__())
print("取到钱 %s 万" %atm.__next__())'''
# yield 就是可以使函数中断，并保存终端状态，中断后，代码可以继续往下执行，过一段时间还可以再重新调用这个函数
# 从上次yield的下一句开始执行

# 代码中n = 0,a = 0,b = 1
# 第一次n =0时，n < max，a = b=1 ,b =a+b =2 n =n+1=1
# 循环5次
# def fab(max):
#     n,a,b = 0 ,0,1
#     while n < max:
#         print(b)
#         a,b = b,a+b
#         n = n + 1
#
# for max in range(5):
#     fab(max)
#
# def fab(max):
#     n,a,b =0,0,1
# # 查看性能cProfile
# import  cProfile
# # cProfile.run()查看某个函数运行暂用的性能
# # cProfile.run("fab(max)")
#
# for i in range(100):
#     print(i)
# cProfile.run("i")

# 另外，还可以通过yield实现在单线程的情况下实现并发运算的效果




# 生产者消费者模型
# 例如: 一个做包子, 两个吃包子
# 首先定义一个吃包子
# send语法,把一个值发送给另一个函数
# yield可以返回值,也可以接收值
# 异步示例:
import time


def consumer(name):  # 第五步
    print("%s 准备吃包子啦！" % name)
    while True:
        baozi = yield

        print("包子[%s]来了，被[%s]吃了" % (baozi, name))


def producer(name):  # 第一步
    c = consumer("A")  # 第二步调用consumer函数，并把函数返回值传给c
    c2 = consumer("B")  # 第三步调用consumer函数，并把函数返回值传给c
    c.__next__()  # 第四步执行生成器步骤
    c2.__next__()
    print("老子开始准备做包子啦！")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子！")
        c.send(i)   # send方法,把A和0传给包子
        c2.send(i)


producer("alex")  # 调用producer函数传人实参
