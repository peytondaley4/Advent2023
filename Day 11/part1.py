# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 23:51:25 2023

@author: Peyton Daley
"""
import copy

f = open('input.txt')

galaxies = []
data = f.read().split('\n')
data = list(list(x) for x in data[:len(data)-1])
c = copy.deepcopy(data)
count = 0

for i in range(len(data)):
    dots = True
    for j in range(len(data[i])):
        if data[i][j] != '.':
            dots = False
    if dots:
        c.insert(i + count, ['.'] * len(data[i]))
        count += 1
        
data = copy.deepcopy(c)

count = 0
for i in range(len(data[0])):
    dots = True
    for j in range(len(data)):
        if data[j][i] != '.':
            dots = False
    if dots:
        for j in range(len(data)):
            c[j].insert(i+count+1, '.')
        count += 1
    
data = c

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == '#':
            galaxies.append((i,j))
         
total = 0
for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        x1 = galaxies[i][1]
        y1 = galaxies[i][0]
        x2 = galaxies[j][1]
        y2 = galaxies[j][0]
        total += abs(x1-x2) + abs(y1-y2)
        
print(total)