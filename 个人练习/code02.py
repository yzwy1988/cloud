from code01 import *
haha('span',8)
def pand(x,y):
    if x > y:
        print 'x 大于y'
    elif x< y:
        print 'x小于y'
    else :
        print x ,"and",y,"are equal"
a =raw_input('请输入一个数字：')
b =raw_input('请在次输入一个数字：')
pand(a,b)
def jia(x,y):
    print  ("x+y结果是:"),x+y
def jian(x,y):
    print ("x-y结果是:"),x-y
def chen(x,y):
    print ("x*y结果是:"),x*y
def chu(x,y):
    print  ("x/y结果是:"),x/y
def panduan(x,o,y):
    if o =="+":
        jia(x, y)
    elif o=="-":
        jian(x, y)
    elif o=="*":
        chen(x, y)
    elif o=="/":
        chu(x, y)
    else:
        pass

a =input("输入一个数字")
b =raw_input("请输入一个符号")
c =input("请输入一个数字")
panduan(a,b,c)

