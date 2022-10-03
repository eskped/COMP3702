# -*- coding: utf-8 -*-
"""
Assignment 0 template

For submission, rename this file to "A0.py" 

Answer each question in the corresponding method definition stub below
"""


def Q1(A,B):
    union = set()
    intersection = set()
    
    union = { x for x in A }
    for y in B:
        union.add(y)
    intersection = A.intersection(B)
    return union,intersection


def Q2(A,B):
    for x in A:
        if x in B:
            print('INTERSECTING')
            return 'INTERSECTING'
    print('DISJOINT')
    return 'DISJOINT'


def Q3(a,b):
    X = set()
    X = { x for x in range(0,a) }
    Y = set()
    Y = { y for y in range(0,b) }
    G = set()
    G = { (x,y) for x in X for y in Y }
    return X,Y,G



def Q4(E,n):
    n_successors = set()
    for e in E:
        if E[e][0] == n:
            n_successors.add(E[e][1])
    return n_successors


def Q5(inFile,outFile,remove):
    f = open(inFile, "r")
    g = open(outFile, "w")
    
    for x in f.read():
        if x != remove:
            g.write(x)
    
    g.close()
    print('Character '+remove+' removed from '+inFile)
    print('Output written to '+outFile)

# Q5("input.txt", "output.txt", '.')

def Q6(state1,state2):
    state1 = list(state1)
    state2 = list(state2)
    
    if (len(state1) or len(state2)) != 9:
        print('IMPOSSIBLE')
        return
    
    chars = ['1','2','3','4','5','6','7','8','_']
    if set(chars) != set(state1):
        print('IMPOSSIBLE')
        return
    
    if set(chars) != set(state2):
        print('IMPOSSIBLE')
        return
    
    startIndex = state1.index('_')
    endIndex = state2.index('_')      
    
    if (abs(startIndex - endIndex) == 3) and (state1[endIndex] == state2[startIndex]):
        if startIndex < endIndex:
            print("D")
        else:
            print("U")
    elif (abs(startIndex-endIndex) == 1) and (state1[endIndex] == state2[startIndex]):
        if startIndex % 3 == 1:
            if startIndex < endIndex:
                print("R")
            else:
                print("L")
        elif startIndex % 3 == 0:
            if startIndex < endIndex:
                print("R")
            else:
                print('IMPOSSIBLE')
        elif startIndex % 3 == 2:
            if startIndex > endIndex:
                print("L")
            else:
                print('IMPOSSIBLE')
    else:
        print('IMPOSSIBLE')
    
# start = "1234_5678"
# end = "1_3425678"
    
# Q6(start, end)