# /usr/bin/env python
# -*- coding:utf-8 -*-


# 迭代器
# 特点:
# 1.访问者不需要关心迭代器内部的结构,进需通过next()方法不断取下一个内容,
# 2.不能随机访问集合中的某个值,只能从头到尾依次访问
# 3.访问到一半时不能回退
# 4.便于循环比较大的数据集合,节省内存

with open('test','r') as f:
    a = f.readlines()
    print(a)
    pa = iter(a)
    print(pa.__next__())

# 用__next__取迭代器里的值,最后没有就报错了
p = iter([1,2,3])
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())

