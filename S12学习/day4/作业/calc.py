# /usr/python/env python
# -*- coding:utf-8 -*-


import re


def get_brackers(input_nums):   # 获取传入字符串外层括号内的所有字符
    find_brackers = re.search("\(.*[\d|\+|\-|*|/|%].*\)", input_nums)
    if find_brackers:
        return find_brackers.group()        # 获取所有带括号的元素


def kuohao(input_nums):     # 获取传入字符串第一个内层括号内的所有字符
    m = re.search("\([\s\d|\.|\+|\-|\*|/|%]*\)", input_nums)
    if m:
        return m.group()        # 返回第一组内容


def add_sub(arg):
    arg = arg.replace('--', '+')    # 同减为加
    arg = arg.replace('++', '+')    # 同加为加
    arg = arg.replace('+-', '-')    # 加减为减
    arg = arg.replace('-+', '-')    # 减加为减
    return arg


def result(arg):     # 每次只处理一个同级别的运算操作,级同一个括号内的,或者是一个没有括号的运算操作
    flag = 0    # 初始化一个结果
    new_str = str(arg).strip('(,)') # 去除括号
    if not re.findall("[\*|/|%]+", new_str):     # 如果是纯加减运算
        new_str = add_sub(new_str)   # 先去除特殊连续运算符号
        new_list = re.findall('[\+|\-]+[\d|\.]+|[\d|\.]+', new_str) # 对字符串进行加减运算
        for i in new_list:
            flag += float(i)
        return float(flag).__round__(16)
    else:    # 对字符串进行乘除运算
        new_str = re.search('[\d|\.]*[\*|/|%|\*\*|//]+[\-]*[\d|\.]+', arg)  # 优先匹配的决定优先级高低
        if new_str:
            new_str = new_str.group()
            if len(new_str.split('/')) > 1: # 处理整除运算
                flag = float(new_str.split('/')[0]) / float(new_str.split('/')[1])
            elif len(new_str.split('*')) > 1:   # 乘法运算
                flag = float(new_str.split('*')[0]) * float(new_str.split('*')[1])
            new_str = arg.replace(new_str, str(flag))
            return result(new_str)
        else:
            return arg


def main(arg):
    brac = get_brackers(arg)    # 获取所有的带括号里面的内容
    if brac:     # 如果获取到的内容带括号
        m = kuohao(brac)    # 获取第一组括号的内容
    else:
        m = re.findall('.*', arg)[0]     # 如果没有输入括号的内容, 取列表的第一个元素,即所有的内容
    res = result(m)  # 开始执行算术
    arg = str(arg).replace(str(m), str(res))     # 把每次的计算结果替换掉表达式内容
    if re.findall('[\+|\*|/|%]+', str(arg)):    # 如果表达式里没有运算符了,则返回,负数除外
        return main(arg)     # 返回最终结算结果
    return arg  # 返回每一次递归后替换的结果


if __name__ == "__main__":
    input_nums =input("请输入计算公式进行计算:")
    # "1-2*((60-30+(-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))"
    print(main(input_nums))     #将格式化后的数据传入主函数模块处理
