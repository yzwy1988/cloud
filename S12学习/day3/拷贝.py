#/usr/bin/env python
#coding=utf-8

# 深浅拷贝

import copy
# 浅拷贝
# copy.copy()
# 深拷贝
# copy.deepcopy()
# 赋值
a = 1

# 数据类型：python里字符串，数字为一种类型。
a1 = 123123
b1 = 123123
# a1和b1指向的内存地址都是一样的
print(id(a1))
print(id(b1))
# 如果a2 = a1 内存地址也是一样的
a2 = a1
print(id(a2))
# 使用浅拷贝,内存地址也是一样的
a3 = copy.copy(a1)
print(id(a3))
# 使用深拷贝,内存地址也是一样的
a4 = copy.deepcopy(a1)
print(id(a4))
# 由此可以得出，拷贝赋值内存地址都不变

# 其他，元组，列表，字典。
n1 = {"k1":'wu','k2':123,'k3':['alex',456]}
# 赋值内存地址都是一样的
n2 = n1
print(id(n1))
print(id(n2))

# 浅拷贝,内存地址就不一样，拷贝的时候只拷贝了一层，字典里的元素没有拷贝
n3 = copy.copy(n1)
print(id(n1))
print(id(n3))
# 只拷贝了字典，字典里的元素没有拷贝
print(id(n1['k3']))
print(id(n3['k3']))
# 浅拷贝只拷贝元组，字典，列表，字符串，数字不拷贝

# 深拷贝，在内存地址中将所有的数据重新创建一份（排除最后一层，即：python内部对字符串和数字的优化）
# 深拷贝地址也不一样
n4 = copy.deepcopy(n1)
print(id(n1))
print(id(n4))
# 字典里的元素id也不一样，内存地址也变化了
print(id(n1['k3']))
print(id(n4['k3']))
'''
import copy

dic = {
    "CPU": [80,],
    "men": [80,],
    "disk": [80,]
}
print('before', dic)

# 使用深拷贝的方法将新的机器CPU改变，老机器的不会变
new_dic = copy.deepcopy(dic)
new_dic["CPU"][0] = 50
print(dic)
print(new_dic)
'''
