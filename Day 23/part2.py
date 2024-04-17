# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 11:25:59 2023

@author: Peyton Daley
"""
def find_path(start, grid, visited = set()):
    dirs = [(0,1), (0,-1), (1,0), (-1, 0)]
    while(start != (len(grid[0]) - 2, len(grid) - 1)):
        turns = []
        if start in visited:
            return 0
        visited.add(start)
        if start == (127, 137):
            start = (127, 138)
            continue
        for d in dirs:
            nex = (start[0] + d[0], start[1] + d[1])
            if nex in visited:
                continue
            char = grid[nex[1]][nex[0]]
            if char == '#':
                continue
            if char == '.':
                visited.add(start)
                start = nex
                break
            elif (char == '>' or char == 'v'):
                visited.add(start)
                turns.append(nex)
        d = 0
        for t in turns:
            v = visited.copy()
            d = max(d, find_path(t, grid, v))
        if len(turns) != 0:
            return d
    return len(visited)
            
f = open('input.txt')

data = list(list(x) for x in f.read().strip().split('\n'))
start = (1,0)
print(find_path(start, data))
