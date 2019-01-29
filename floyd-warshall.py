# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 10:02:55 2018

@author: Ezekiel Marvin
"""

import numpy as np

inf = float('inf')

def floydwarshall(a):
    n = len(a)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                a[i][j] = min(a[i][j], a[i][k] + a[k][j])
        print(np.matrix(a))
        
    "print(np.matrix(a))"
    
floydwarshall([[0,1,4,inf],[1,0,2,4],[4,2,0,1],[inf,4,1,0]])
            