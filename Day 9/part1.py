# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:29:39 2023

@author: Peyton Daley
"""

def test_list(l):
    for val in l:
        if val != 0:
            return False
    return True

def extrapolate(data):
    vals = [data]
    while not test_list(vals[-1]):
        temp = []
        for i in range(len(vals[-1])-1):
            temp.append(vals[-1][i+1] - vals[-1][i])
        vals.append(temp)
    vals[-1].append(0)
    for i in reversed(range(len(vals)-1)):
        vals[i].append(vals[i+1][-1] + vals[i][-1])
    return vals[0][-1]
            
f = open('input.txt')

data = []

for line in f:
    data.append(list(int(x) for x in line.split()))
    
total = 0
for d in data:
    total += extrapolate(d)
    
print(total)