# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 10:28:58 2023

@author: Peyton Daley
"""
def intersect(blocks, index):
    block = blocks[index]
    for i in range(len(blocks)):
        b = blocks[i]
        count = 0
        if i == index:
            continue
        for i in range(3):
            if type(b[i]) is tuple and type(block[i]) is tuple:
                s1 = set(range(b[i][0], b[i][1]+1))
                s2 = set(range(block[i][0], block[i][1]+1))
                if len(s1.intersection(s2)) != 0:
                    count += 1
            elif type(b[i]) is tuple:
                s = range(b[i][0], b[i][1]+1)
                if block[i] in s:
                    count += 1
            elif type(block[i]) is tuple:
                s = range(block[i][0], block[i][1]+1)
                if b[i] in s:
                    count += 1
            else:
                if b[i] == block[i]:
                    count += 1
        if count == 3:
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
                temp.append((top[i], bottom[i]))
            else:
                temp.append((bottom[i], top[i]))
        else:
            temp.append(top[i])
    blocks.append(temp)

count = 1
while count != 0:
    count = 0
    for i in range(len(blocks)):
        b = blocks[i]
        if type(b[2]) is not tuple:
            if b[2] == 1:
                continue
            b[2] -= 1
            if intersect(blocks, i):
                b[2] += 1
            else:
                count += 1
        if type(b[2]) is tuple:
            if b[2][0] == 1:
                continue
            b[2] = (b[2][0]-1, b[2][1]-1)
            if intersect(blocks, i):
                b[2] = (b[2][0]+1, b[2][1]+1)
            else:
                count += 1
    print(count)
print(blocks)
        
    