# coding=utf-8
#!C:\Python27\python2.exe


# python3的语法
print("geek")
print("super")
print("super \ntwo")
a = 2
b = a
a = 10
print(a, b)
print(id(a), id(b))  # 内存地址不相同
# a的变量变化后，b的不会变，a的变量被回收了，b指向a后面有被回收，变量的作用，指在内存中保存的作用
a = [1, 2, 3]
b = a
a[1] = 5
print(a, b)
print(id(a), id(b))   # 内存地址相同

name = input("Please your name:")
print("You name is :%s" % name)
sex = input("Please input your gender:")
# ==是判断，=号是变量 python是通过缩进来决定代码块
if sex == "girl":
    print("I would like to have a little monkeying")
elif sex == "man":
    print("Going to homosexual!...")
else:
    print("Pervert!")
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
