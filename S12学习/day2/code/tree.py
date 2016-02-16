# -*-coding:utf-8-*-
# author:shen
# DATE:2016/1/28


filename = open('goods.txt', 'w+')
for line in filename:
    if line.startswith("alex"):
        new_line = line.replace("alex", "ALEX LI")
        filename.write(new_line)
        print(filename)
filename.close()
