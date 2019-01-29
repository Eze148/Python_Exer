# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 19:55:03 2018

@author: Ezekiel Marvin
"""
#Highest Common Factor
a =eval(input("Input 1st Number: "))
b =eval(input("Input 2nd Number: "))
c=a
d=b
if c>d:
    while d>=0:
        if a % d == 0 and b%d==0:
            print(d,"is the highest common factor of",a,"and",b)
            break
        d=d-1
elif d>c:
    while c>=0:
        if a % c == 0 and b%c==0:
            print(c,"is the highest common factor of",a,"and",b)
            break
        c=c-1
        