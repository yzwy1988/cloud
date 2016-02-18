# -*-coding:utf-8-*-
# author:shen
# DATE:2016/2/18



def login(func):
    def wrapper(*arg, **kwargs):
        ret = func(*arg, **kwargs)
        return ret
    return wrapper


def show():
    return 'show'

# show,show()是不一样的，show（）是找到函数执行函数，show是指向内存不执行
new_show = login(show)