# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 13:42:28 2018

@author: Ezekiel Marvin
Hamilton Minimum Cycle
"""

# G = {'A':{'A':0, 'B':7, 'C':2, 'D':8, 'E':3, 'F':4},
#      'B':{'A':7, 'B':0, 'C':7, 'D':5, 'E':9, 'F':3},
#      'C':{'A':2, 'B':7, 'C':0, 'D':4, 'E':8, 'F':6},
#      'D':{'A':8, 'B':5, 'C':4, 'D':0, 'E':7, 'F':6},
#      'E':{'A':3, 'B':9, 'C':8, 'D':7, 'E':0, 'F':7},
#      'F':{'A':4, 'B':3, 'C':6, 'D':6, 'E':7, 'F':0}}

# G = {'A':{'A':0, 'B':5, 'E':10},
#      'B':{'A':5, 'B':0, 'C':2, 'D':3, 'E':3},
#      'C':{'B':2, 'C':0, 'D':7, 'E':4},
#      'D':{'B':3, 'C':7, 'D':0, 'E':5},
#      'E':{'A':10,'B':3, 'C':4, 'D':5, 'E':0}}

# G = {'A':{'A':0, 'B':5, 'C':3},
#      'B':{'A':5, 'B':0, 'C':2},
#      'C':{'B':2, 'C':0, 'A':3}}

# G = {'A':{'A':0, 'B':5, 'C':3, 'D':1},
#      'B':{'A':5, 'B':0, 'C':2, 'D':1},
#      'C':{'B':2, 'C':0, 'A':3, 'D':7},
#      'D':{'A':1, 'B':1, 'C':7, 'D':0}}

G = {'A':{'B':5, 'A':0},
     'B':{'B':0}}

def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths
    
def find_cycle(graph,startnode):
    cycles=[]
    for endnode in graph:
        newpaths = find_all_paths(graph, startnode, endnode)
        for path in newpaths:
            if (len(path)==len(graph)):
                if path[0] in graph[path[len(graph)-1]]:
                    path.append(path[0])
                    cycles.append(path)     
    cost(cycles)
    print(len(cycles))
    return mm(graph,cycles)
    
def cost(cycles):
    for end in cycles:
        cost = 0
        x = 0
        for path in end:
            if x == 0:
                paths = path
            cost = cost + G[paths][path]
            x=x+1
            paths = path
        end.append(cost)    
        
def mm(graph,cycles):
    minims = []
    for i in range(len(cycles)):
        if i == 0:
            minimal = cycles[i]
        elif(cycles[i][len(graph)+1] < minimal[len(graph)+1]):
            minimal = cycles[i]
            minims = []
        elif(cycles[i][len(graph)+1] > minimal[len(graph)+1]):
            if i == len(cycles)-1:
                minims.append(minimal)
                continue
        elif(cycles[i][len(graph)+1] == minimal[len(graph)+1]):
            minims.append(minimal)
            minimal = cycles[i]
        if i == len(cycles)-1:
            minims.append(minimal)
    if minims == []:
        print("Hamilton Cycle Does not Exist")
        return
    return minims
                  
print(find_cycle(G,'A'))