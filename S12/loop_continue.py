# /usr/bin/env python
# -*-coding:utf-8 -*-

for j in range(5):
    for i in range(10):
        if i < 5:
            continue
            # 如果小于5，就跳出本次循环
        if j > 3:
            # 大于3就结束打印i
            break
        print(i)
