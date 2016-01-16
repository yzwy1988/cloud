#coding=utf-8
import os
import time

for file in os.listdir('C:\\Users\\PCPC\\Desktop\\SVNDB\\code'):
    print file

'''with open('C:\\Users\\PCPC\\Desktop\\11.dic','rt') as f:
    data =f.read()
    print data
'''
def loadDataSet(filename):
    dataMat=[]
    fr=open(filename)
    for line in fr.readlines():
        line = line.replace('"','')
        curLine=line.strip().split('\t')
        aa = [(i) for i in curLine]
        dataMat.append(aa)
    return dataMat
dataMat=loadDataSet('C:\\Users\\PCPC\\Desktop\\11.dic')
print (dataMat)    

with open(name, mode='r', buffering=1)