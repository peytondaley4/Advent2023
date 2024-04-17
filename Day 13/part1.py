# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 01:18:11 2023

@author: Peyton Daley
"""

def find_mirror(grid):
    for i in range(len(grid)-1):
        mirror = True
        for j in range(len(grid[0])):
            if grid[i][j] != grid[i+1][j]:
                mirror = False
        if mirror:
            left = i - 1
            right = i + 2
            while (left >= 0 and right < len(grid) and mirror):
                for j in range(len(grid[0])):
                    if grid[left][j] != grid[right][j]:
                        mirror = False
                left -= 1
                right += 1
            if mirror:
                return 100 * (i + 1)
            
    for i in range(len(grid[0])-1):
        mirror = True
        for j in range(len(grid)):
            if grid[j][i] != grid[j][i+1]:
                mirror = False
        if mirror:
            left = i - 1
            right = i + 2
            while (left >= 0 and right < len(grid[0]) and mirror):
                for j in range(len(grid)):
                    if grid[j][left] != grid[j][right]:
                        mirror = False
                left -= 1
                right += 1
            if mirror:
                return i + 1

f = open('input.txt')

grids = []
grid = []
for line in f:
    if line.strip() == '':
        grids.append(grid)
        grid = []
        continue
    grid.append(list(line.strip()))
grids.append(grid)
    
total = 0
for grid in grids:
    total += find_mirror(grid)

print(total)