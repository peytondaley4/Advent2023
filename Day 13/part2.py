# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 01:18:11 2023

@author: Peyton Daley
"""

def find_mirror(grid, hlimit, vlimit):
    p1 = 0
    for i in range(len(grid)-1):
        if i == hlimit:
            continue
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
                p1 = 100 * (i + 1)
            
    for i in range(len(grid[0])-1):
        if i == vlimit:
            continue
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
                return (p1, i + 1)
    return (p1,0)

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
    
vals = []
for grid in grids:
    vals.append(find_mirror(grid, len(grid), len(grid[0])))
        

total = 0
for k in range(len(grids)):
    grid = grids[k]
    val = 0
    for i in range(len(grid)):
        if val != 0:
            break
        for j in range(len(grid[0])):
            if grid[i][j] == '.':
                grid[i][j] = '#'
            else:
                grid[i][j] = '.'
            val = find_mirror(grid, vals[k][0] // 100 - 1, vals[k][1] - 1)
            val = max(val)
            if val != 0:
                total += val
                break
            val = 0
            if grid[i][j] == '.':
                grid[i][j] = '#'
            else:
                grid[i][j] = '.'

print(total)