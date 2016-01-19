# /usr/bin/env python
# coding=utf-8


# 列表 切片取值
name_list = ['alex', 'brother', 'tenglan']
print(name_list[1])
# 输出 brother取值
enumerate(name_list)
# help(name_list)
# 查看有什么方法
name_list.append("tenglan")
print(name_list)
# index 索引
print(name_list.index("alex"))
# count统计
print(name_list.count("tenglian"))
# 指定位置插入和值
name_list.insert(2, "88")
print(name_list)
# pop删除最后一个
name_list.pop()
print(name_list) \
    # remove指定删除，要指定值
name_list.remove('88')
print(name_list)
# 反转排序
name_list.reverse()
print(name_list)
# 排序sort
name_list.sort()
print(name_list)
name_list.append("hi")
name_list.append("bs")
name_list.sort()
print(name_list)
# 循环遍历删除
for i in range(name_list.count('alex')):
    name_list.remove("alex")
    print(name_list)
# 切片
a = [1, 2, 3, 'a', 'b']
# 切除1-2的要定位到3
print(a[0:3])
a.insert(2, 4)
print(a)
a.insert(5, 5)
print(a)
print(a[0:2])
b = [1, 2, 3, 'a', 'b']
# 去最后一个
print(b[-1])
# 取前三个
print(b[0:3])
# 取最后两个
print(b[-2:])
c = b[0:3]
print(c)

# 扩展
print(a + b + c)
# 或者a.extend(b)
print(a.extend(b))
name = "shen"
a.extend(name_list)
# 强大的扩展
print(a.extend(name))
# 判断是否在列表里
print('bs' in a)

# 元祖
t = (1, 2, 3, 4)
# 元祖转换列表
print(list(t))
