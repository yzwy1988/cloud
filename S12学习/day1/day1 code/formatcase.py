# /usr/bin/env python
# -*-coding:utf-8-*-


# 格式化一个字符串的输出结果，我们在很多地方可以看到
# 下面看看python中的字符串格式化函数str.format():
# 使用str.format()函数
# 使用{}占位符
li = input('please input name:')
print('#' * 40)
print('#   i\'m {},{}'.format(li, 'Welcome to my space!      #'))
print('#' * 40)

# 也可以使用{0}，{1}形式的占位符
print('{0},I\'m {1},my E-mail is {2}'.format("Hello","shen","888@gamil.com"))
print('#' * 40)
# 可以改变占位符的位置,在传入参数时也要根据位置写入
print('{1},I\'m {0},My E-mail is {2}'.format('shen','hello','888@gmail.com'))
print('#' * 40)

# 使用{name}形式的占位符
print('Hi,{name},{message}'.format(name='Tom',message='How old are you?'))
print('#' * 40)


table = {'Sjoerd':4127,'Jack':4098,"Dcab":7678}
for name,phone in table.items():
    print('{0:10} ===> {1:10}'.format(name,phone))


def bubble_sort(lists):
    count = len(lists)
    for i in range(0,count):
        for j in range(i + 1,count):
            if lists[i] > lists[j]:
                lists[i],lists[j] = lists[j],lists[i]
    return lists

bubble_sort([11,22,33])