# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 13:47:25 2018

@author: Ezekiel Marvin
"""

for a in range(1,10001):
    c=a
    d=[]
    e=0
    while c>0:
        if a%c ==0:
            d.append(c)
        c=c-1
    n=len(d)-1
    while n>=0:
        if d[n] == a:
            pass
        else:
            e=e+d[n]
        n=n-1
    if e == a:
        print(a,"is a perfect number.")
    else:
        pass
    