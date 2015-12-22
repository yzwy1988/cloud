'''
i = int(raw_input('净利润:'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
#这是输出一个列表
#print arr
for idx in range(0,6):
#这个其实就是把idx带入到arr中，每次取arr一个值.运用列表a[1],a[2]...
#print arr[idx]
#print rat[idx]
    if i>arr[idx]:
	r +=(i-arr[idx])* rat[idx]
	print (i-arr[idx]) * rat[idx]
	i =arr[idx]
print '奖金为:%.f'% r

#120000 - 100000 * 0.075'''
# --*-- coding:utf8 --*--

# i = int(raw_input('净利润:'))
arr = [10, 20, 40, 60, 100]
rat = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]
r = 0

i = 26
locate = 0
print len(arr)
for index in range(len(arr)):
    print index, arr[index]
    if (i > arr[index]) and (i < arr[index+1]):
        locate = index
        print "locate", locate

array_1 = []
for a in range(len(arr)):
    deta = [10, 10, 20, 20, 40]
    array_1.append(deta[a] * rat[a])

value = 0
for a in range(locate+1):
    value = value + array_1[a]

print value + (i - arr[locate])*rat[locate+1]
