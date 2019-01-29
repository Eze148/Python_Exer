# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 09:32:03 2018

@author: Ezekiel Marvin
"""
import numpy as np

def warshall(a):
    'assert (len(row) == len(a) for row in a)' 
    n = len(a)
    for m in range(n):
        a[m][m]= 1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                a[i][j] = a[i][j] or (a[i][k] and a[k][j])
                
    print(np.matrix(a))

warshall([[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,1,0,0]])