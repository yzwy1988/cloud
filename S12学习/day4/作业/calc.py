# /usr/python/env python
# -*- coding:utf-8 -*-




def get_brackers(string):
    find_brackers = re.search("\(.*[\d|\+|\-|*|/|%].*\)", string)
    if find_brackers:
        return find_brackers.group()


def kuohao(string):
    m = re.search("\([\s\d|\.|\+|\-|\*|/|%]*\)", string)
    if m:
        return m.group()


def add_sub(arg):
    arg = arg.replace('--', '+')
    arg = arg.replace('++', '+')
    arg = arg.replace('+-', '-')
    arg = arg.replace('-+', '-')
    return arg


def result(arg):
    flag = 0
    new_str = str(arg).strip('(,)')
    if not re.findall("[\*|/|%]+", new_str):
        new_str = add_sub(new_str)
        new_list = re.findall('[\+|\-]+[\d|\.]+|[\d|\.]+', new_str)
        for i in new_list:
            flag += float(i)
        return float(flag).__round__(16)
    else:
        new_str = re.search('[\d|\.]*[\*|/|%|\*\*|//]+[\-]*[\d|\.]+', arg)
        if new_str:
            new_str = new_str.group()
            if len(new_str.strip('/')) > 1:
                flag = float(new_str.split('/')[0]) / float(new_str.split('/')[1])
            elif len(new_str.split('*')) > 1:
                flag = float(new_str.split('*')[0]) * float(new_str.split('*')[1])
            new_str = arg.replace(new_str, str(flag))
            return result(new_str)
        else:
            return arg


def main(arg):
    brac = get_brackers(arg)
    if brac:
        m = kuohao(brac)
    else:
        m = re.findall('.*', arg)[0]
    res = result(m)
    arg = str(arg).replace(str(m), str(res))
    if re.findall('[\+|\*|/|%]+', str(arg)):
        return main(arg)
    return arg


if __name__ == "__main__":
    import re

    string = "1-2*((60-30+(-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))"
    print(main(string))
