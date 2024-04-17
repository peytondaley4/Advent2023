# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 10:28:58 2023

@author: Peyton Daley
"""
def intersect(blocks, index):
    block = blocks[index]
    for i in range(len(blocks)):
        b = blocks[i]
        if index == i:
            continue
        for el in b:
            if el in block:
                return True
    return False

f = open('input.txt')
blocks = []
for line in f:
    top = line.split('~')[0].split(',')
    top = list(int(x) for x in top)
    bottom = line.strip().split('~')[1].split(',')
    bottom = list(int(x) for x in bottom)
    temp = []
    for i in range(3):
        if top[i] != bottom[i]:
            if top[i] < bottom[i]:
                top, bottom = bottom, top
            temp2 = bottom.copy()
            for j in range(bottom[i], top[i]+1):
                temp2[i] = j
                temp.append(temp2.copy())
    if temp == []:
        temp.append(bottom)
    blocks.append(temp)

count = 1
while count != 0:
    count = 0
    ground = False
    for i in range(len(blocks)):
        b = blocks[i]
        for el in b:
            if el[2] == 1:
                ground = True
                break
        if ground:
            ground = False
            continue
        for el in b:
            el[2] -= 1
        if intersect(blocks, i):
            for el in b:
                el[2] += 1
        else:
            count += 1
            
    print(count)
print(blocks)
        
    