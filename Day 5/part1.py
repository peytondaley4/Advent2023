# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 00:06:37 2023

@author: Peyton Daley
"""

def source_to_dest(seeds, start, dest, rang):
    result = []
    for seed in seeds:
        test = False
        for i in range(len(start)):
            if seed in range(start[i], start[i] + rang[i]):
                test = True
                result.append(seed - start[i] + dest[i])
        if not test:
            result.append(seed)
    return result

f = open('input.txt')
line1 = f.readline()
seeds = list(map(int, line1.split(':')[1].split()))
f.readline()
data = f.read().split('\n')

start = []
dest = []
rang = []

for line in data:
    if line == '':
        seeds = source_to_dest(seeds, start, dest, rang)
        continue
    if line[0].isalpha():
        start = []
        dest = []
        rang = []
        continue
    start.append(int(line.split()[1]))
    dest.append(int(line.split()[0]))
    rang.append(int(line.split()[2]))
    
print(min(seeds))