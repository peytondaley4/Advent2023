# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 23:43:01 2023

@author: Peyton Daley
"""

def check_pos(pos):
    for p in pos:
        if p[2] != 'Z':
            return False
    return True

f = open('input.txt')

dirs = list(f.readline().strip())
f.readline()

turns = dict()
pos = []

for line in f:
    key = line.split()[0]
    if key[2] == 'A':
        pos.append(key)
    ldir = line.split()[2][1:4]
    rdir = line.split()[3][:3]
    turns[key] = (ldir, rdir)

steps = 0

while not check_pos(pos):
    for d in dirs:
        if check_pos(pos):
            break
        for i in range(len(pos)):
            if d == 'L':
                pos[i] = turns[pos[i]][0]
            if d == 'R':
                pos[i] = turns[pos[i]][1]
        steps += 1
        if steps % 100000 == 0:
            print(steps)
        
print(steps)