# /usr/bin/env python
# -*- coding:utf-8 -*-

# 写入文件
"""
f = open('test.log', 'w')
f.write('Helloworld,测试写入内容')
f.close()


# 读取文件方法1
# python3按照字符读取,python2按字节读取
a = open('test.log', 'r',encoding='utf-8')
ret = a.read(14)  # 用read读取5个字符
print(ret)
a.close()  # 关闭文件

# 读取文件方法2
# 避免打开文件忘记关闭,可以通过管理上下文的方法,with open() as f:的方法
with open('test.log','r') as f:
    a = f.readline()
    print(a)"""

with open('test.log','r') as f:
    f.seek(4)       # 指定指针位置在第四个字节
    print(f.tell())  # 获取当前指针位置是4,一个汉字3个字节,字母符号一个字节,所以读取完后位置就是4
    print(f.readline())  # 从第四个字节开始读取一行
# flush 刷新文件内部缓存区
# next()获取下一行数据,不存在,则报错
# read读取指定字符数据
# readline 仅读取一行数据
# readlines 读取所有数据,并根据换行保存值列表
# seek 指定文件中指针位置
# tell 获取当前指针位置,按字符移动
# writelines 将一个字符串列表写入文件
# readable 是否可读
# truncate 截取数据,仅保留指定之前数据
# python3中读取文件read是按字符读取的,seek()指定指针位置是按字节指定的


