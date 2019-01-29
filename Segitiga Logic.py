# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:28:32 2018

@author: Ezekiel Marvin
"""

a = eval(input("Enter a high number: "))
b = eval(input("Enter a number: "))
c = eval(input("Enter a number: "))
if a > b+c:
    print('Bukan Segitiga')
elif a==b or a==c or b==c:
    if a==b and b==c:
        print('Segitiga Sama Sisi')
    else:
        print('Segitiga Sama Kaki')
elif a**2 == b**2 + c**2:
    print('Segitiga Siku-Siku')
else:
    print('Segitiga Sembarang')