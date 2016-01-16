#coding=utf-8
import math

def print_twice(bruce):
    print bruce
    print bruce
    
print_twice("Spam")
print_twice("29")
print_twice(math.pi)
print_twice(math.pi*8)
print_twice("\nSpam"*4)
print_twice(math.cos(math.pi))
michael ='Eric,the half a bee'
print_twice(michael)

def cat_twice(part1,part2):
    cat=part1+part2
    print_twice(cat)
    
line1 ='Bing tiddle'
line2 ='Tiddle bang'
cat_twice(line1,line2)

from math import pi
print math
print type(math)
print pi

def right_justify(s):
    print '                                          '+s

right_justify('allen')
    
def do_so(f):
    print f
    print f
    
def print_sp(one,two):
    cat =one+two
    do_so(cat)
    
a1 ='diyigezhi'
a2 ='diergezhi'
print_sp(a1,a2)

def do_twice(f,a):
    print f,a
    print f,a
    
def print_spam():
    print 'spam'
    
pa ='spam2'
do_twice(print_spam,pa)

print '+','----','+','----','+'
print '|'