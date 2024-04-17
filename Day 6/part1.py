# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 12:48:10 2023

@author: Peyton Daley
"""
import math

f = open('input.txt')

times = list(map(int, f.readline().split()[1:]))
dists = list(map(int, f.readline().split()[1:]))
counts = []

for i in range(len(times)):
    left = math.floor(times[i] / 2)
    right = math.ceil(times[i] / 2)
    while (left * right > dists[i]):
        left -= 1
        right += 1
    count = right - left - 1
    counts.append(count)

total = 1    
for count in counts:
    total *= count

print(counts)
print(total)