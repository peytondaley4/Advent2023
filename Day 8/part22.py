# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 23:43:01 2023

@author: Peyton Daley
"""
from math import gcd

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
loops = []

for line in f:
    key = line.split()[0]
    if key[2] == 'A':
        pos.append(key)
    ldir = line.split()[2][1:4]
    rdir = line.split()[3][:3]
    turns[key] = (ldir, rdir)

for p in pos:
    steps = 0
    pairs = []
    while p[2] != 'Z':
        for i in range(len(dirs)):
            if p[2] == 'Z':
                break
            pairs.append((p, i))
            if dirs[i] == 'L':
                p = turns[p][0]
            if dirs[i] == 'R':
                p = turns[p][1]
            steps += 1
    loops.append(steps)

print(loops)

lcm = 1
for l in loops:
    lcm = lcm*l//gcd(lcm,l)

print(lcm)