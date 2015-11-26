#coding=utf-8
from sys import argv


#argv的使用,在输入中的值传给变量script ,user_name
script,user_name = argv
#参数1，参数2 = argv #之后参数的引用就和这个先后顺序有关了
prompt ='>'
print " My name is %s," % user_name
print 'And you know i am the %s script,'% script
print " do u like me?"
like = raw_input(prompt)
print ' how od r u?'
age = raw_input(prompt)
print """
OK,you said you %r me very much,you r %r years old
"""%(like,age)

 
 