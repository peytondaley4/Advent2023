# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 00:06:37 2023

@author: Peyton Daley
"""

def source_to_dest(seeds, start, dest, rang):
    result = []
    extra = seeds.copy()
    for seed in seeds:
        for i in range(len(start)):
            left = max(seed[0], start[i])
            right = min(seed[1], start[i] + rang[i])
            lleft = min(seed[0], start[i])
            lright = min(seed[1], start[i]) - 1
            rleft = max(seed[0], start[i] + rang[i]) + 1
            rright = max(seed[1], start[i] + rang[i])
            if right >= left:
                result.append((left - start[i] + dest[i], right - start[i] + dest[i]))
                if (seed[0], seed[1]) in extra:
                    extra.remove((seed[0], seed[1]))
            if right >= left and lright >= lleft and (lleft, lright) not in seeds:
                seeds.append((lleft, lright))
                extra.append((lleft, lright))
            if right >= left and rright >= rleft and (rleft, rright) not in seeds:
                seeds.append((rleft, rright))
                extra.append((rleft, rright))
    for seed in extra:
        if seed not in result:
            result.append(seed)
    return result

f = open('input.txt')
line1 = f.readline()
line1 = list(map(int, line1.split(':')[1].split()))
seeds = []
for i in range(int(len(line1) / 2)):
    seeds.append((line1[2*i], line1[2*i+1] + line1[2*i]))

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
    
print(min(seeds)[0])