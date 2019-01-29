# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 11:37:19 2018

@author: Ezekiel Marvin
"""
import math
def py(x, y=10):
     pi_calc=1
     sqr2=0
     for i in range(x,y):
         sqr2=math.sqrt(2+sqr2)
         pi_calc=pi_calc*sqr2/2
         pi=2/pi_calc
         print(pi)
(py(0))