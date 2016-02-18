# -*-coding:utf-8-*-
# author:shen
# DATE:2016/2/18


# day4
#
# 迭代器 1
# 生成器 2
# 装饰器 2
# 递归   2
# 正则表达式 2
# 基础算法（了解）
# 常用模块
# json.loads() pickle
# 作业：计算器





# 迭代器完美解释

# 需求
li = [11, 22, 33, 44, 55]
print(li[:])
# 1、如果python语言没有for，怎么循环
# 用while去循环
i = len(li)
start = 0
# i =0 =false 其他都是true，如果大于0就可以循环了
while i > start:
    print(li[start])
    start += 1
#########################################
# 本质
# for item in li:
#     print(item)
# 使用本质，创建一个for循环,
obj = iter(li)
while True:
    try:
        item = obj.__next__()
        print(item)
    except Exception:
        pass


##########################################

# 第一步执行了 obj = iter（li）
# 第二步 print（obj.__next__())方法

# for循环的本质
# 1.创建一个特殊的东西（就是迭代器），获取到一个具有next方法的对对对象
# 2.根据这个东西，去操作列表li中的内容

# 迭代器是什么 iter()就是迭代器
# 执行迭代器返回一个对象，对象是含有next方法

# 打印元素

# 循环
# 1、 while
#     索引，下标取数据，随意取值
# 2、for
#     a.执行迭代器，获取一个对象
#     b.执行对象的next方法
#
# 引出，迭代器
# iter，获得一个具有next方法的对象
# 只能按顺序拿




# 生成器 （非常非常非常重要）
# python2.7     range xrange
# python3   一个range
# 区别
# range（10） --->  立马在内存里创建0-9
# xrange(10)  ---->  内存里没有数字
#  for i in xrange()
#    第一次循环内存里创建 0
#    i = 0
#     第二次循环内存里创建1
#     i =1
#   print(i)



def show():
    yield 'line1'
    yield 'line2'
    yield 'line3'


my_f = show()
for line in my_f:
    print(line)

# 总结：
#      迭代器：next，for，执行next方法
#      1.函数如果含有yield，函数返回值特殊的东西（必须和for一起使用）被迭代
#      2.for，函数返回的特殊，函数内部执行代码，如果遇到yield关键字就会冻结当前状态，跳出函数
#        回到for，特殊对象的位置，for的一次循环完成之后
#        再次进入函数，回到上一次执行的代码位置，继续往下执行

# 生成器有两点：
#     1.必须迭代执行生成器
#     2.yield冻结状态（基础上一次执行的位置）




f = open('f.log', 'r')
for line in f:
    print(line)


# 文件操作也类似这样



# 装饰器 --必备
# 装饰器就是一个函数，装饰其他函数



def login(func):
    def wrapper(*arg, **kwargs):
        ret = func(*arg, **kwargs)
        return ret

    return wrapper


def show():
    return 'show'


# show,show()是不一样的，show（）是找到函数执行函数，show是指向内存不执行
new_show = login(show)


# 递归

# 俄罗斯套玩


def function():
    print('1')
    function()


function()

# 第一次执行function


# 正则
# 处理字符串
# 规则： \s => 空格
#       \d => 数字

# 如：找到所有的数字
# 1.字符串规则
# 2.次数规则



# re.match() match重头去匹配 \d+ 出现1次或多次
# re.search() search搜任意位置去匹配
# re.sub()  替换
# re.split 分组
# 如果没有匹配到，返回值None
# 匹配到了
# group
# groups括号可以用来分组，第一个匹配规则就在第一组里，第二个在第二组
import re
a ="123abc456"
ret1 = re.search("[0-9]*",a).group()
ret2 = re.search("([0-9]*)([a-z]*)([0-9]*)",a).group()
ret3 = re.search("[0-9]*[a-z]*[0-9]*",a).group()
ret4 = re.sub('\d+','sb',a)
ret5 = re.split('\d+',a)
print(ret1, ret2, ret3,ret4, ret5)

