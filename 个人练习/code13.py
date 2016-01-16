#coding = utf-8
#冒泡排序
#line 4:定义一个乱序的列表list
array = [1,2,5,3,6,8,4]
'''line 7:这就是上边给的例子的第二条，我们替换下就成为range(6,1,-1)，意思是从6到1间隔-1,
也就是倒叙的range(2,7,1),随后把这些值循环赋给i，那么i的值将会是[6, 5, 4, 3, 2]'''
for i in range(len(array)-1,0,-1):
    print i
    #line 10:这是一个循环赋值给j，j的值将会是[0, 1, 2, 3, 4, 5][0, 1, 2, 3, 4][0, 1, 2, 3][0, 1, 2][0, 1]'''
    for j in range(0,i):
        print j
        #line 13：其实·就是使用这个把这个没有顺序的array = [1, 2, 5, 3, 6, 8, 4]排序'''
        if array[j] > array[j + 1]:
            #line 15：array[j], array[j + 1] = array[j + 1], array[j] 替换赋值'''
            array[j],array[j+1] = array[j+1],array[j]
            print 'i:',i, 'j:', j, '-->', array            
#print array


#map(function, sequence) 为每一个元素依次调用 function(item) 并将返回值组成一个链表返回
def cube(x): 
    print x*x*x

map(cube,range(1,11))

#列表推导式为从序列中创建列表提供了一个简单的方法。
#普通的应用程序通过将一些操作应用于序列的每个成员并通过返回的元素创建列表，或者通过满足特定条件的元素创建子序列
squares = []
for x in range(10):
    squares.append(x**2)
print squares



#使用sort一句就可以搞定
hp = [1,2,5,3,6,8,4]
hp.sort()
print hp