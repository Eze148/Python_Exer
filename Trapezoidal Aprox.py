# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 14:22:57 2018

@author: Ezekiel Marvin
"""

b = eval(input("Batas atas: "))
a = eval(input("Batas bawah: "))
n=10
ym=0
m = (b-a)/n
print(m)
m1= a
wy=0
print(m1)
for i in range(0,n+1):
    l=(m1+i*m)
    ym = l
    if i == 0 or i == n:
        w = 1
    else:
        w=2
    wy = wy+ w * ym

print(wy)