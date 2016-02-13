# coding=utf-8
 # /usr/bin/env python

lucky_num = 19
input_num = -1

guess_count = 0

# 加上次数限制
while guess_count < 3:
    input_num = int(input("Input the guess num:"))
    if input_num > lucky_num:
        print("the real numer is smaller.")
    elif input_num < lucky_num:
        print("the real numer is bigger..")
    else:
        print("bingo")
        break
    guess_count += 1
else:
    print("猜错了")
