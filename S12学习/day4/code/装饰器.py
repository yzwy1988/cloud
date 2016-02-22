# -*-coding:utf-8-*-
# author:shen
# DATE:2016/2/18


# 装时期(必备)
def login(func):
    def wrapper(*arg, **kwargs):
        ret = func(*arg, **kwargs)
        return ret

    return wrapper


def show():
    return 'show'


# show,show()是不一样的，show（）是找到函数执行函数，show是指向内存不执行
new_show = login(show)

# # 第一波
# def foo():
#     print("foo")
#
# foo  # 表示是函数
# foo()   # 表示执行foo函数
#
# # 第二波
# def foo():
#     print("foo")
#
# foo = lambda x: x + 1
# foo()   # 执行下面的lambda表达式,而不在是原来的foo函数,因为函数foo被重新定义了

# 非装饰器实现

'''
def login(func):
    print("passed user verification...")
    return func   # tv函数存放在内存中


def home(name):
    print("welcome [%s] to home page" %name)


def tv(name):
    print("welcome [%s] to tv page" %name)


def move(name):
    print("welcome [%s] to move page"%name)


tv = login(tv)
tv('Alex')  # 给tv传入参数
move = login(move)
move('Shen')
home = login(home)
home('baike')'''


# 执行login函数,tv会传给login(func),执行完return func,tv会放在内存中,在执行tv()函数,打印语句!

# 装饰器方法实现


def login(func):
    def inner(*args):
        print("passed user verification...")
        func(*args)  # func函数存放在内存中,*args,可以传入多个参数或者一个参数

    return inner


@login
# @函数就执行这句先调用login函数
# 给home传入多个参数,在fun(*args)添加*
def home(name, passwd):
    print("welcome [%s] to home page [%s]" % (name, passwd))


def tv(name):
    print("welcome [%s] to tv page" % name)


def move(name):
    print("welcome [%s] to move page" % name)


home("Yamaha", "Super")


# 函数是第一类对象
def fun(a, b):
    return (a + b)


add = fun  # 第一种方式：add = fun，fun函数赋值给add变量


# print(add(1,2))  add（）传参数求值return和fun啊（）一样
# print(fun(1,2))
def caller_func(f):
    return f(1, 2)


if __name__ == "__main__":
    print(caller_func(fun))

''' 将函数对象作为参数，传递给另一个函数
可以看到func作为参数传递给caller_func函数，传参过程类似于一个赋值操作f=fun；
于是fun函数对象，被caller_fun函数作用域中的局部变量f引用，f实际指向了函数fun；
当执行return f（1，2）的时候，相当于执行了 return fun（1，2）；因此输出结果是3
'''

'''
函数对象vs函数调用
无论是把函数复制给新的标识符，还是作为参数传递给新的函数，针对的都是函数本身，而不是函数的调用
用一个更加简单，但从外观上看，更容易产生混淆的例子来说明这个问题，例如定义了下面这个函数：
'''
def func():
    return "hello world"

# 然后分别执行两次赋值
ref1 = func  # 将函数对象赋值给ref1
ref2 = func()   #调用函数，将函数的返回值（“hello world”）赋值给ref2

# 很多初学者都会混淆这两种赋值，通过python内建的type函数，可以查看一下这两次赋值的结果
print(type(ref1))    # 返回类型function
print(type(ref2))    # 返回类型str
# 可以看到，ref1引用了函数对象本身，而ref2则引用了函数的返回值，通过内建的
# callable函数，可以进一步验证ref1是可调用的，而ref2是不可调用的
print(callable(ref1))    # True
print(callable(ref2))    # False
# 传参的效果与之类似


# 闭包&LEGB法则
# 所谓闭包，就是将组成函数的语句和这些语句的执行环境打包在一起时，得到的对象

# 听上去的确有些复杂，还是用一个例子来帮助理解一下，假设我们在foo.py模块中做了如下定义：
filename = "foo.py"
def call_func(f):
    return f()  # 如前面介绍的，f引用一个函数对象，然后调用它


# 在另一个func.py模块中，写下了这样的代码：
import foo

filename = "func.py"

def show_filename():
    return "filename:%s" % filename
if __name__ == "__name__":
    print(foo.call_func(show_filename))  # 注意：实际发生调用的位置，是在foo.call_func函数中
# 当我们用python func.py命令执行func.py时输出结果为：
# python func.py
# 很显然show_filename（）函数使用的filename变量的值，是在与它相同环境（func.py模块）中定义的那个。尽管
# foo.py模块中也定义了同名的filename变量，而且实际调用show_filename的位置也是在foo.py的call_func内部

# 而对于嵌套函数，这一机制则会表现的更加明显：闭包将会捕捉内层函数执行所需的整个环境：

# 而对于嵌套函数,这一机制则会表现的更加明显：闭包将会捕捉内层函数执行所需的整个环境:

# enclosed.py
import foo
def wrapper():
    fileename ="enclosed.py"
    def show_filename():
        return "filename: %s"%filename
    print(foo.call_func(show_filename))    # 输出:filename:enclosed.py

# 实际上，每一个函数对象，都有一个指向了该函数定义时所在全局名称空间的__globals__属性：
著作权归作者所有。
商业转载请联系作者获得授权，非商业转载请注明出处。
作者：陈伟
链接：https://www.zhihu.com/question/25950466/answer/31731502
来源：知乎
'''
#show_filename inside wrapper
#show_filename.__globals__
{
'__builtins__': <module '__builtin__' (built-in)>,        #内建作用域环境
'__file__': 'enclosed.py',
'wrapper': <function wrapper at 0x7f84768b6578>,      #直接外围环境
'__package__': None,
'__name__': '__main__',
'foo': <module 'foo' from '/home/chiyu/foo.pyc'>,         #全局环境
'__doc__': None
}'''

# 当代码执行到show_filename中的return "filename：%s"%filename语句时，解析器按照下列的顺序查找filename变量：
# local -本地函数（show_filename）内部，通过任何方式赋值的，而且没有被global关键字声明为全局变量的filename变量;
# Enclosing -直接外围空间（上层函数wrapper）的本地作用域，查找filename变量（如果有多层嵌套，则由内而外逐层查找，直至最外层的函数）；
# Global - 全局空间（模块enclosed.py），在模块顶层复制的filename变量；
# Builtin - 内置模块（__builtin__)中预定义的变量名中查找filename变量；
# 在任何一层先找到符合要求的filename变量，则不在像更外层查找。如果直到Builtin层仍然没有找到符合要求的变量，则抛出NameError异常。
# 这就是变量名解析的：LEGB法则

# 总结：
# 1.闭包最重要的使用价值在于：封存函数执行的上下文环境；
# 2.闭包在其捕捉的执行环境（def语句块所在上下文）中，也遵循LEGB规则逐层查找，直至找到符合要求的变量，或者抛出异常。


# 装饰器&语法糖（syntax sugar）
# 那么闭包和装饰器又有什么关系呢？
# 上问题到闭包的重要特性：封存上下文，这一特可以巧妙的被用于现有函数的包装，从而为现有函数更加功能。而这就是装饰器。
