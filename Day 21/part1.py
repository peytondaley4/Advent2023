# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 10:56:36 2023

@author: Peyton Daley
"""
f = open('input.txt')
data = list(list(x) for x in f.read().strip().split('\n'))
points = set()
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 'S':
            points.add((i, j))
           
for k in range(500):
    new_points = set()
    count = 0
    for line in data:
        for el in line:
            if el == 'O':
                count += 1
    print(count, k)
    for point in points:
        i = point[0]
        j = point[1]
        if i > 0 and data[i-1][j] != '#':
            data[i-1][j] = 'O'
            new_points.add((i-1, j))
        if i < len(data)-1 and data[i+1][j] != '#':
            data[i+1][j] = 'O'
            new_points.add((i+1, j))
        if j > 0 and data[i][j-1] != '#':
            data[i][j-1] = 'O'
            new_points.add((i, j-1))
        if j < len(data[0])-1 and data[i][j+1] != '#':
            data[i][j+1] = 'O'
            new_points.add((i, j+1))
        data[i][j] = '.'
    points = new_points.copy()