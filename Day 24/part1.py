# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 09:41:16 2023

@author: Peyton Daley
"""
def intersect(stone1, stone2, domain):
    pos1, pos2 = stone1[0], stone2[0]
    vel1, vel2 = stone1[1], stone2[1]
    m1, m2 = vel1[1] / vel1[0], vel2[1] / vel2[0]
    b1 = pos1[1] - vel1[1] * pos1[0] / vel1[0]
    b2 = pos2[1] - vel2[1] * pos2[0] / vel2[0]
    if m1 == m2:
        return False
    int_x = (b2-b1)/(m1-m2)
    int_y = m1 * int_x + b1
    if int_x < pos1[0] and vel1[0] > 0:
        return False
    if int_x > pos1[0] and vel1[0] < 0:
        return False
    if int_x < pos2[0] and vel2[0] > 0:
        return False
    if int_x > pos2[0] and vel2[0] < 0:
        return False
    if domain[0] <= int_x <= domain[1] and domain[0] <= int_y <= domain[1]:
        return True
    return False

f = open('input.txt')
stones = []
for line in f:
    pos = list(int(x) for x in line.split('@')[0].split(', '))
    vel = list(int(x) for x in line.split('@')[1].split(', '))
    stones.append((pos, vel))

count = 0
domain = (200000000000000,400000000000000)
for i in range(len(stones)):
    for j in range(i+1, len(stones)):
        if intersect(stones[i], stones[j], domain):
            count += 1
            
print(count)