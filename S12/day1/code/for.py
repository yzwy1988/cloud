# coding=utf-8
# /usr/bin/env python

lucky_num = 19
input_num = -1

for i in range(3):
    input_num = int(input("Input the guess num:"))
    if input_num > lucky_num:
        print("the real numer is smaller.")
    elif input_num < lucky_num:
        print("the real numer is bigger..")
    else:
        print("bingo")
        break
else:
    print("猜错了")
