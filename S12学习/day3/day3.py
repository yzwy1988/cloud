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
import collections

Mytuple = collections.namedtuple('Mytuple', ['x', 'y', 'z'])
print(Mytuple)
