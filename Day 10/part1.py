# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 23:59:33 2023

@author: Peyton Daley
"""

f = open("input.txt")

data = f.read().split('\n')

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 'S':
            start_pos = (i,j)
            
loop =  [start_pos]

loop_len = 0
curr_pos = start_pos

up = ['J', '|', 'L', 'S']
left = ['J', '-', '7', 'S']
down = ['7', '|', 'F', 'S']
right = ['-', 'F', 'L', 'S']

while curr_pos != start_pos or loop_len == 0:
    y = curr_pos[0]
    x = curr_pos[1]
    char = data[y][x]
    if y > 0 and char in up and ((y-1, x) not in loop or ((y-1, x) == start_pos and loop_len > 1)) and data[y-1][x] in down:
        loop.append((y-1,x))
        curr_pos = (y-1,x)
    elif x > 0 and char in left and ((y, x-1) not in loop or ((y, x-1) == start_pos and loop_len > 1)) and data[y][x-1] in right:
        loop.append((y,x-1))
        curr_pos = (y,x-1)
    elif y < len(data) - 1 and char in down and ((y+1, x) not in loop or ((y+1, x) == start_pos and loop_len > 1)) and data[y+1][x] in up:
        loop.append((y+1,x))
        curr_pos = (y+1,x)
    elif x < len(data[0]) - 1 and char in right and ((y, x+1) not in loop or ((y, x+1) == start_pos and loop_len > 1)) and data[y][x+1] in left:
        loop.append((y,x+1))
        curr_pos = (y,x+1)
    loop_len += 1
    
print(loop_len/2)