# /usr/bin/env python
# coding=utf-8


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
