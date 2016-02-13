# coding=utf-8


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
