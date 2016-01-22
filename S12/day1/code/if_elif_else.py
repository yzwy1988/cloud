# coding=utf-8


# 猜lucky number， n =6
# 猜的数字比6大，提示你打印小一点
# 猜的数字比6小，提示你打印大一点
# 猜得数字等于6，提示bingo
# python3.x以后，input返回的是字符串，执行强制类型转换int(input())
# 只要猜不对，就一直猜，直到才对为止使用while True
# 猜对了就结束判断，添加break
# 第一种写法
lucky_num = 6
while True:
    num = int(input("Please input lucky number:"))

    if num == lucky_num:
        print("恭喜你，猜对了%s！Bingo" % num)
        break
    elif num < lucky_num:
        print("你猜错了，猜的数字%s太小了！" % num)
    # else是上面的判断都不满足，才会用，不用输入条件
    else:
        print("你猜错了，猜得数字%s太大了！" % num)


# 第二种不使用break
lucky_num = 6
num = -1
while lucky_num != num:
    num = int(input("Please input lucky number:"))

    if num == lucky_num:
        print("恭喜你，猜对了%s！Bingo" % num)
        # break
    elif num < lucky_num:
        print("你猜错了，猜的数字%s太小了！" % num)
    # else是上面的判断都不满足，才会用，不用输入条件
    else:
        print("你猜错了，猜得数字%s太大了！" % num)


# 第三种写法，如果不想等，就执行输入的内容，判断大于还是小于，不要用else判断
lucky_num = 6
num = -1
while lucky_num != num:
    num = int(input("Please input lucky number:"))

    # if num == lucky_num:
    # print("恭喜你，猜对了%s！Bingo" % num)
    # break
    if num < lucky_num:
        print("你猜错了，猜的数字%s太小了！" % num)
    # else是上面的判断都不满足，才会用，不用输入条件
    elif num > lucky_num:
        print("你猜错了，猜得数字%s太大了！" % num)
print("恭喜你才对了%s！Bingo" % num)

