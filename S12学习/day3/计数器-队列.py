# coding=utf-8


# 一.collections计数器
# counter是对字典类型的补充,用于追踪值得出现次数
# 具备字典的所有功能和自己的功能
import collections

obj = collections.Counter("absbdbsbdasbdabdsadhads")
print(obj)
# 输出 Counter({'d': 6, 'b': 6, 'a': 5, 's': 5, 'h': 1})
# 计数器的功能
ret = obj.most_common(2)
print(ret)
# 输出取前两位[('b', 6), ('d', 6)]
for k, v in obj.items():
    print(k, v)
# 输出值
# s 5
# a 5
# h 1
# d 6
# b 6
for k in obj.elements():
    print(k)
# elements原生的值
# obj处理完的值


# 创建一个列表
obj1 = collections.Counter(['11', '22', '33', '44'])
print(obj1)
# 更新
obj1.update(['eric', '11', '22'])
print(obj1)
# 删除,如果不存在的出现次数显示为负数
obj1.subtract(['11', '11', 'eric', 'eric'])
print(obj1)

# 二.有序字典(orderedDict)
# OrderedDict是对字典类型的补充,他记住了字典元素添加的顺序
# 字典 dic ={'k1':'v1','k10':'v10'}
# 列表 li = k1...k10
# 构建一个有序字典
# for i in li:
#     print(dict[i])
# 实现一个有序字典
dic = collections.OrderedDict()
dic['k1'] = 'v1'
dic['k2'] = 'v2'
dic['k3'] = 'v3'
print(dic)
# 有序字典的方法和字典的是一样的
# dic.pop()拿取指定的一个
# dic.popitem()按顺序拿，后进先出
# dic.setdefault('k11')默认值
# print(dic)
# dic.update({'k1':'v111','k10':'v10'}) # 更新
# # dic.move_to_end('k1') 把k1拿到最后
# print(dic)

# 三.默认字典(defaultdict)
# defaultdict是对字典的类型补充，他默认给字典的值设置一个类型
# 设置字典的值默认是一个列表
# dic = collections.defaultdict(list)
# dic['k1'].append('alex')
# print(dic)

'''
from collections import defaultdict

values = [11, 22, 33, 44, 55, 66, 77, 88]
# 定义默认为字典方法
my_dict = defaultdict(list)

for value in values:
    if value > 66:
        my_dict['k1'].append(value)
    else:
        my_dict['k2'].append(value)
print(my_dict)
'''

# 四.可命名元组（namedtuple）
# 根据namedtuple可以创建一个包含tuple所有功能以及其他功能的类型
# 元组不可以修改


import collections

# 创建类 等同于defaultdict
MytupleClass = collections.namedtuple('MytupleClass', ['x', 'y', 'z'])
print(MytupleClass)
# 查看对象有哪些方法使用(help(MytupleClass))
print(help(MytupleClass))
# 创建对象
obj = MytupleClass(11, 22, 33)
print(obj.x)
print(obj.y)
print(obj.z)
# 对象都有哪些功能
# _asdict() 返回一个字符串
# _replace() 指定值替换成谁

# 五.双向队列（deque）
# 一个线程安全的双向队列
# 双向队列可以进可以取
# 创建双向队列
d = collections.deque()
# 方法
# append()添加
# appendleft 左边添加
# clear清空队列
# count计算某个元素除了多少次
d.append('1')
d.appendleft('10')
d.appendleft('1')
print(d)
# 查看1出现了几次，使用count，输出2次
r = d.count('1')
print(r)
# extend扩展
d.extend(['yy','uu','ii'])
print(d)
# extendleft左边扩展
d.extendleft(['love','you','me'])
print(d)
# index取这个值的索引位置
print(help(d))
# inster 插入
# pop取数据
# popleft左边取
# remove 删除
# reverse 反转
# rotare 从右边那数据插入左边，执行5次操作
d.rotate(5)

# 单项队列
# 注：既然有双向队列，也有单项队列（先进先出FIFO)
# Queue.queue

import queue
# 创建单项队列
q = queue.Queue()
# 插入数据,要加参数
q.put('123')
q.put('678')
# 数据的个数
print(q.qsize())
# 放数据，不需要加参数，要按他的单项队列去放
print(q.get())
