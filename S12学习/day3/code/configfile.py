# /usr/bin/env python
# -*- coding:utf-8 -*-

# startswith 是否以某个字段开头的
import json


def check(backend):
    check_list = []
    flag = False
    with open('back', 'r') as f:
        for line in f:
            if line.startswith('backend'):
                if backend == line.strip().split()[1]:  # strip 换行,split 去掉空格
                    flag = True
                    continue
            if flag and line.startswith('backend'):
                break
            if flag and line.strip():
                check_list.append(line)
    return check_list


def add(inp_dic):
    add_mess = 'server %s weight % maxconn % ' % (inp_)


def menu():
    print('''
    ****************
    1  查看数据
    2  添加数据
    3  删除数据
    ****************
    ''')


def main():
    menu()
    action = input('请选择操作序号:')
    if action == '1':
        backend = input('''请按如下格式输入要操作的字段:
        www.oldboy.org
        ''')
        check(backend)
    if action == '2':
        inp_data = input('''
        请按如下格式输入要操作的字段:
        server 100.1.7.9 100.1.7.9 weight 20 maxconn 3000
        ''')
        inp_dic = json.loads()


if __name__ == '__main__':
    main()
