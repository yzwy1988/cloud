#coding=utf-8
import math
i =1
for i in range(100):
    print i*math.pi/360

def Pink():
    print "I'm  very like python"
    print 'Beijing to china'
    
def make():
    Pink()
    Pink()
    
make()

rec ={'name':{'first':'Bob','last':'smith'},
      'job':['dev','mgi'],
      'age':40}
print rec['name']
print rec['neme']['last']