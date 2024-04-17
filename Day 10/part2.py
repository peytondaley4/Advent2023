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

fix_s = []
if (start_pos[0]-1, start_pos[1]) in loop and data[start_pos[0]-1][start_pos[1]] in down:
    fix_s.append(set(up))
if (start_pos[0]+1, start_pos[1]) in loop and data[start_pos[0]+1][start_pos[1]] in up:
    fix_s.append(set(down))
if (start_pos[0], start_pos[1]-1) in loop and data[start_pos[0]][start_pos[1]-1] in right:
    fix_s.append(set(left))
if (start_pos[0], start_pos[1]+1) in loop and data[start_pos[0]][start_pos[1]+1] in left:
    fix_s.append(set(right))
sets = fix_s[0].intersection(fix_s[1])
char = sets.pop()
if char == 'S':
    char = sets.pop()
data[start_pos[0]] = data[start_pos[0]].replace('S', char)

insides = []
for i in range(len(data)):
    out = True
    dirs = ''
    for j in range(len(data[i])):
        if (i,j) in loop:
            char = data[i][j]
            if char == '-':
                continue
            elif char == '|':
                out = not out
            elif char == '7' and dirs != 'L':
                out = not out
            elif char == 'F':
                dirs = 'F'
                out = not out
            elif char == 'J' and dirs != 'F':
                out = not out
            elif char == 'L':
                dirs = 'L'
                out = not out
        elif not out:
            insides.append((i,j))

for i in range(len(data)):
    for j in range(len(data[i])):
        if (i,j) in loop:
            print(data[i][j], end = '')
        elif (i,j) in insides:
            print(' ', end = '')
        else:
            print(' ', end = '')
    print()