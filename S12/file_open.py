# /usr/bin/env python
# -*-coding:utf-8-*-

# 打开文件
# file_obj = file("文件路径"，"模式")
# 3.x打开的方式
# file_obj = open("文件路径","模式")

# 打开文件的模式
# r以只读方式打开
# w打开一个文件只用与写入，如果该文件已存在则将其覆盖，如果该文件不存在就创建新文件
# a打开一个文件用于追加,如果该文件已存在,文件指针将会放在文件的结尾,也就是说,如果该文件在不存在,创建新文件进行写入
# w+打开一个文件用于写入,如果该文件已存在则将其覆盖,如果该文件不存在,创建新文件



# 读取文件
# 一次性加载所有内容到内存
# obj.read()
# 一次性加载所有内容到内存，并根据行分割成字符串
# obj.readlines()

# 每次仅读取一行数据
# for line in obj:
#     print line

# 写文件的内容
# obj.write("内容")

# 关闭文件句柄
# obj.close()



# 打开文件
f = open("test.log", "w")
# write覆盖以前的文件，创建新的文件
# 写入文件
f.write("This is the first line\n")
f.write("This is the second line\n")
f.write("this is the 3 line\n")
f.write("this is the 4 line\n")
f.close()

# 读取文件,模式为r
f = open('test.log', 'r')
for line in f:
    if "5" in line:
        print("this is the third line")
    else:
        print(line),
f.close()

# 写入文件,用于追加 a模式
# 写的模式下读取也会报错
f = open("test.log", "a")
f.write("hello")
f.close()
# 在读取
f = open("test.log", 'r')
print(f.read())
f.close()

# 写读模式
# 写读会把原来的内容清掉
f = open("test.log", "w+")
f.write("new line\n")
print(f.readline())
f.close()
