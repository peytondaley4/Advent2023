# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 11:25:59 2023

@author: Peyton Daley
"""
def find_path(start, grid, visited = set()):
    dirs = [(0,1), (0,-1), (1,0), (-1, 0)]
    while(start != (len(grid[0]) - 2, len(grid) - 1)):
        turns = 0
        turn = ''
        for d in dirs:
            nex = (start[0] + d[0], start[1] + d[1])
            char = grid[nex[1]][nex[0]]
            if char == '#':
                continue
            if char == '.' and nex not in visited:
                visited.add(start)
                start = nex
                break
            elif (char == '>' or char == 'v') and d in [(0,1), (1,0)]:
                turn = char
                visited.add(start)
                turns += 1
        if turns >= 2:
            v1 = visited.copy()
            v2 = visited.copy()
            v1.add((start[0], start[1]+1))
            v2.add((start[0]+1, start[1]))
            return max(find_path((start[0], start[1]+2), grid, v1), find_path((start[0]+2, start[1]), grid, v2))
        if turns == 1:
            if turn == '>':
                visited.add((start[0] + dirs[2][0], start[1] + dirs[2][1]))
                start = (start[0] + 2 * dirs[2][0], start[1] + 2 * dirs[2][1])
            if turn == 'v':
                visited.add((start[0] + dirs[0][0], start[1] + dirs[0][1]))
                start = (start[0] + 2 * dirs[0][0], start[1] + 2 * dirs[0][1])
    return len(visited)
            
f = open('input.txt')

data = list(list(x) for x in f.read().strip().split('\n'))
start = (1,0)
print(find_path(start, data))
