# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 15:59:00 2018

@author: Ezekiel Marvin
"""

def eFor(a):
    y=0
    for i in range(1,11):
       y = y -((a**i)/i )

    return y
def ewhile(b):
    z=1
    y=0
    i=1
    while(i<=100 and z!=y):
        z=y
        y = y -((b**i)/i )
        i+=1
        print(y)
    return i

ln = eval(input("Input Ln(): "))
x = 1-ln
print(eFor(x))
print(ewhile(x))
