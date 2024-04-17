# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 23:43:01 2023

@author: Peyton Daley
"""

f = open('input.txt')

dirs = list(f.readline().strip())
f.readline()

turns = dict()

for line in f:
    key = line.split()[0]
    ldir = line.split()[2][1:4]
    rdir = line.split()[3][:3]
    turns[key] = (ldir, rdir)

pos = 'AAA'
steps = 0
while pos != 'ZZZ':
    for d in dirs:
        if pos == 'ZZZ':
            break
        if d == 'L':
            pos = turns[pos][0]
        if d == 'R':
            pos = turns[pos][1]
        steps += 1
        
print(steps)