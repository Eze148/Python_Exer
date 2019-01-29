# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 13:13:44 2018

@author: Ezekiel Marvin
"""
import math
t=True
while(t==True):
    print("Menu")
    print("(1) Sin")
    print("(2) Cos")
    print("(3) Tan")
    print("(0) Exit")
    a = eval(input("Pick a Menu(0-3): "))
    n=10
    temp = 0
    if a == 0:
        t=False
    elif a == 1:
        thet=eval(input("Input the Angle in degree: "))
        x = math.pi*thet/180
        #print(x)
        for i in range (0,n):
           temp = temp+(((-1)**i)*(x**(2*i+1))/math.factorial(2*i+1))
        #result = math.sin(x)
        result = temp
        print(result)
    elif a == 2:
        thet=eval(input("Input the Angle in degree: "))
        x = math.pi*thet/180
        for i in range (0,n):
            temp=temp+(((-1)**i)*(x**(2*i))/math.factorial(2*i))
        #result = math.cos(x)
        result = temp
        print(result)
    elif a == 3:
        thet=eval(input("Input the Angle in degree: "))
        x = math.pi*thet/180
        temps = 0
        tempc = 0
        for i in range (0,n):
            temps=temps+(((-1)**i)*(x**(2*i+1))/math.factorial(2*i+1))
            tempc=tempc+(((-1)**i)*(x**(2*i))/math.factorial(2*i))
        #result = math.tan(x)
        temp=temps/tempc
        result = temp
        print(result)
    else:
        print("Try Again")
    