# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 12:48:10 2023

@author: Peyton Daley
"""
import math

f = open('input2.txt')

nums = f.readline().split()[1:]
time = ''
for num in nums:
    time += num
time = int(time)

dists = f.readline().split()[1:]
dist = ''
for dis in dists:
    dist += dis
dist = int(dist)

left = math.floor(time / 2)
right = math.ceil(time / 2)
while (left * right > dist):
    left -= 1
    right += 1
count = right - left - 1

print(count)