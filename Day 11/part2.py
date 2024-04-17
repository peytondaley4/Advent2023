# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 23:51:25 2023

@author: Peyton Daley
"""
f = open('input.txt')

galaxies = []
data = f.read().split('\n')
data = list(list(x) for x in data[:len(data)-1])
l = 1000000

for i in range(len(data)):
    dots = True
    for j in range(len(data[i])):
        if data[i][j] != '.':
            dots = False
    if dots:
        for j in range(len(data[i])):
            data[i][j] = l

for i in range(len(data[0])):
    dots = True
    for j in range(len(data)):
        if data[j][i] not in  ['.', l]:
            dots = False
    if dots:
        for j in range(len(data)):
            data[j][i] = l

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == '#':
            galaxies.append((i,j))

total = 0
for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        y1 = galaxies[i][0]
        y2 = galaxies[j][0]
        x1 = galaxies[i][1]
        x2 = galaxies[j][1]
        dist = 0
        for k in range(y1+1, y2 + 1):
            if data[k][x1] in ['.', '#']:
                dist += 1
            else:
                dist += data[k][x1]
        for k in range(min(x1,x2)+1, max(x1,x2) + 1):
            if data[y1][k] in ['.', '#']:
                dist += 1
            else:
                dist += data[y1][k]
        total += dist
        
print(total)