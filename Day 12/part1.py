# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 15:12:28 2023

@author: Peyton Daley
"""
from functools import lru_cache

@lru_cache
def find_sols(row, run):
    row = list(row)
    run = list(run)
    if row.count('#') > sum(run):
        return 0
    if row.count('#') + row.count('?') < sum(run):
        return 0
    if len(run) == 0 and row.count('#') == 0:
        return 1
    if len(run) == 0:
        return 0
    if len(row) == 0:
        return 0
    search = run[0]
    length = 0
    sols = 0
    for i in range(len(row)):
        char = row[i]
        if char == '.' and length == 0:
            continue
        if char == '#':
            length += 1
            if length == search and (i == len(row) - 1 or row[i + 1] != '#'):
                if i != len(row) - 1 and row[i+1] == '?':
                    row1 = ['.']
                    row1 = row1 + row[i+2:]
                    return find_sols(tuple(row1), tuple(run[1:]))
                return find_sols(tuple(row[i+1:]), tuple(run[1:]))
        elif char == '.':
            return 0
        else:
            row1 = row.copy()
            row1[i] = '.'
            sols += find_sols(tuple(row1), tuple(run))
            row1[i] = '#'
            sols += find_sols(tuple(row1), tuple(run))
            break
    return sols
        

f = open('input.txt')

rows = []
runs = []

for line in f:
    row = list(line.split()[0])
    run = list(int(x) for x in line.split()[1].split(','))
    row2 = row.copy()
    run2 = run
    for i in range(4):
        row2.append('?')
        row2 = row2 + row
        run2 = run2 + run
    rows.append(row2)
    runs.append(run2)
    
total = 0

for i in range(len(rows)):
    num = find_sols(tuple(rows[i]), tuple(runs[i]))
    print(num)
    total += num
    
print(total)