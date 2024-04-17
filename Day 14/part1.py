# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 00:03:34 2023

@author: Peyton Daley
"""
def roll_north(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                index = 0
                for k in reversed(range(0, i)):
                    if grid[k][j] == 'O' or grid[k][j] == '#':
                        index = k + 1
                        break
                grid[i][j] = '.'
                grid[index][j] = 'O'
                
def roll_west(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                index = 0
                for k in reversed(range(0, j)):
                    if grid[i][k] == 'O' or grid[i][k] == '#':
                        index = k + 1
                        break
                grid[i][j] = '.'
                grid[i][index] = 'O'

def roll_south(grid):
    for i in reversed(range(len(grid))):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                index = len(grid)-1
                for k in range(i+1, len(grid)):
                    if grid[k][j] == 'O' or grid[k][j] == '#':
                        index = k - 1
                        break
                grid[i][j] = '.'
                grid[index][j] = 'O'

def roll_east(grid):
    for i in range(len(grid)):
        for j in reversed(range(len(grid[0]))):
            if grid[i][j] == 'O':
                index = len(grid[0]) -1
                for k in range(j+1, len(grid[0])):
                    if grid[i][k] == 'O' or grid[i][k] == '#':
                        index = k - 1
                        break
                grid[i][j] = '.'
                grid[i][index] = 'O'
            
f = open('input2.txt')

data = list(list(x) for x in f.read().strip().split('\n'))

for i in range(1000000):
    if i % 10000 == 0:
        print(i)
    roll_north(data)
    roll_west(data)
    roll_south(data)
    roll_east(data)

for line in data:
    print(''.join(line))