#coding=utf-8
import xlrd

username =[]
passwd = []



data1 =xlrd.open_workbook('E:\\SVNDB\\code\\user.xlsx')
table = data1.sheets()[0] 
nrows = table.nrows
'''for i in range(nrows ):
    print table.row_values(i)

    
user = [table.row_values(i)[0]]
password = [table.row_values(i)[1]]
for username in user:
    pass
for passwd in password:
    pass
print username,password'''

for i in range(nrows):
    print table.row_values(i)
    username.append(table.row_values(i)[0])
    passwd.append(table.row_values(i)[1])

#print [username[0]]
for loginname in (username[0:]):
    print loginname
for password in (passwd[0:]):
        print password