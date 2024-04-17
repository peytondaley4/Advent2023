# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 23:56:43 2023

@author: Peyton Daley
"""

def hash_str(string):
    curr_val = 0
    for char in string:
        num = ord(char)
        curr_val += num
        curr_val = (curr_val * 17) % 256
    return curr_val

f = open('input.txt')

data = f.readline().strip().split(',')
print(data)
total = 0
for d in data:
    total += hash_str(d)
print(total)