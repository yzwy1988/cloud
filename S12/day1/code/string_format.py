# /usr/bin/env python
# coding=utf-8

name = input("name").strip()  # 去掉空格strip()
age = input("age").strip()
job = input("job").strip()
# 第一种格式化输出
print("information of %s:\n name:%s\n age:%s\n job:%s" % (name, name, age, job))

# 第二种使用+连接起来输出
name = input("name:")
age = input("age:")
job = input("job:")
print("information of []:" + name + "\n name:[]" + name + "\n age:[]" + age + "\n job:[]" + job)

# 第三种多行输出
msg = '''
information of %s:
    name:%s
    age:%s
    job:%s
''' % (name, name, age, job)
print("information of %s:\n name:%s\n age:%s\n job:%s" % (name, name, age, job))

# %s  代表字符串
# %f  代表浮点
# %d 代表整型
