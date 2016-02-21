# /usr/bin/env python
# -*-coding:utf-8-*-


# 正则表达式是对字符串的匹配
# 首先要有一个匹配规则
# 要告诉数据源

import re

#abc匹配规则,abcde是数据源
# 匹配上了就返回object,匹配不上就返回None

# match 是从开头匹配
m = re.match("abc","abcdef")
print(m.group())   # 查看匹配上的数据

# 匹配所有数据0-9 ,0-9只是匹配一个数字,要匹配多个数字可以写成[0-9][0-9],也可以写成{0,10},指定匹配多少次{10}
a = re.match('[0-9]{0,10}','29265abcbdef')
print(a.group())

# findall 匹配所有的数字  ,用findall时,print不需要加group
b = re.findall('[0-9]{0,10}',"2390muming902ngx!")
print(b)
# 匹配出所有字符串
n = re.findall('[a-zA-Z]{1,10}',"2390muming902ngx!")
print(n)

# 匹配所有用(.*)  .
# *就是匹配0个和多个
k = re.findall('.*',"2390muming902ngx!")
# .+匹配1个或多个
k = re.findall('.+',"2390muming902ngx!")
k = re.findall('[a-zA-z]+',"23xd90muming9#0~2ngx!")
# 匹配特殊字符,只能写在规则里去匹配
k = re.findall('_',"2390muming902_~ngx!")
if k:
    print(k)


# search方法,查找整个找到第一个就返回 search需要输出需要加group()
# 匹配一个数字或多个数字是\d+
p = re.search('\d+',"2390muming902_~ngx!")
# 匹配连续的数字
p = re.search('^\d+$',"13800138000")
if p:
    print(p.group())

# sub 替换
# 把所有的数字替换为#
s = re.sub('\d+',"/","23maum2in12g90ad2_~2ng3x!")
# 如果后面的不想替换,只想替换前面两个,后面加count=2
s = re.sub('\d+',"/","23maum2in12g90ad2_~2ng3x!",count=2)
if s:
    print(s)
#  |是或者的意思
j = re.search("\(.*[\d|\+|\-|*|/|%].*\)","20 * 2 - (9 + 1 * 2 - (29 - 8 / 7)*88/9**8)")
print(j.group())
