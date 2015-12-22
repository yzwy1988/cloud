#coding=utf-8
#while循环
i = 0
while True:
    print '已经打印 %s'%i
    i = i + 1
    if i == 100:
        break
else:
    print '推出循环'
print '已经结束循环'
#转义字符打印
print 'hello world \nchina of bank \t superish'
print 'welcome to %s %s'%('python', 'world')
print "%s %d-%d"%('time',2015,12)


for d in range(5):
    print '%.*f'%(d,1.2345678)
#列表推到 矩阵    
a =[[1,2,3],
    [4,5,6],
    [7,8,9]]
crp =[a[i][i] for i in[0,1,2]]
print crp

#字典
D ={'food':'spam','name':'shen','age':20}
print D
print D['food']
D['age'] += 2
print D
#另一种字典定义的方式
P ={}
P['name']='jike'
P['job'] ='dev'
P['like']='music'
print P
print (P['name'])
print P['job']
#重访嵌套
pm ={'name':{'first':'Bob','last':'Lily'},
     'job':['Dev','Ps'],
     'age':30.3}
print pm['name']['first']
print pm['job']
print pm['job'][-1]
pm['job'].append('hack')
print pm['job']
#for循环
Sp ={'a':1,'b':2,'c':3}
print Sp
#先输出列表
ks = list(Sp.values())
print ks
bs = list(Sp.keys())
#在排序
bs.sort()
print bs
#key对应的是a,b,c；所以输出的时候Sp[key]就代表输出Sp[a],Sp[b],Sp[c]的值
for key in bs:
    print key,'==>',Sp[key]
    print Sp[key]
#sorted内置函数对象类型进行排序    
for key in sorted(Sp):
    print (key,'=>',Sp[key])
#for循环就是一个序列操作，他可以使用任意一个序列对象
for c  in 'superstar':
    print (c.upper())
#upper函数将小写转换为大写

#while循环是一种更为常见的排序循环工具，它不仅限于遍历序列

x =4
while x>0:
    print ('Mrak!'* x)
    x -= 1
#列表解析表达式
ms =[x ** 2 for x in [2,3,4,5,6]]
print ms
#通过for循环
ms_1 =[]
for x in [1,2,3,4,5]:
    ms_1.append(x**2)
print ms_1

#元组,元组与列表字典的唯一区别就是不可以变更
T =(1,2,3,4,5)
print len(T)
T+ (6,7)
#元组支持混合的类型和嵌套
k