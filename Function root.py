# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 14:14:14 2018

@author: Ezekiel Marvin
"""

def nroots(n,s):
    xb,x=1000,10
    rang=100
    a=0
    while(xb !=x and a<=rang):
        xb=x
        x = x-(x**n-s)/(n*x**(n-1))
        a+=1
        print(x)
    if(a<=rang):
        return x;
    else:
        return(float('nan'));
        
print(nroots(10,1024))

