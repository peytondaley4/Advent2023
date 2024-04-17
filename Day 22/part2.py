# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 10:28:58 2023

@author: Peyton Daley
"""     
import copy
   
def game_print(game):
    for i in reversed(range(len(game[0][0]))):
        for j in range(len(game)):
            block = False
            for k in range(len(game[0])):
                if game[j][k][i] == 'B':
                    block = True
                    break
            if block:
                print('B', end = '')
            else:
                print('0', end = '')
        print()
    print()
    for i in reversed(range(len(game[0][0]))):
        for j in range(len(game[0])):
            block = False
            for k in range(len(game)):
                if game[k][j][i] == 'B':
                    block = True
                    break
            if block:
                print('B', end = '')
            else:
                print('0', end = '')
        print()
    print()

def intersect(game, block):
    for el in block:
        if game[el[0]][el[1]][el[2]] == 'B':
            return True
    return False

f = open('input.txt')
blocks = []
maxx = 0
maxy = 0
maxz = 0
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
    if top[0] > maxx:
        maxx = top[0]
    if top[1] > maxy:
        maxy = top[1]
    if top[2] > maxz:
        maxz = top[2]
    if temp == []:
        temp.append(bottom)
    blocks.append(temp)
    
game = [[['0' for _ in range(maxz+1)] for _ in range(maxy+1)] for _ in range(maxx+1)]
for block in blocks:
    for el in block:
        game[el[0]][el[1]][el[2]] = 'B'
      
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
            game[el[0]][el[1]][el[2]] = '0'
            el[2] -= 1
        if intersect(game, b):
            for el in b:
                el[2] += 1
                game[el[0]][el[1]][el[2]] = 'B'
        else:
            count += 1
            for el in b:
                game[el[0]][el[1]][el[2]] = 'B'

total = 0
for block in blocks:
    lowest = 0
    for el in block:
        if el[2] < lowest or lowest == 0:
            lowest = el[2]
        game[el[0]][el[1]][el[2]] = '0'
    count = 1
    cgame = copy.deepcopy(game)
    cblocks = copy.deepcopy(blocks)
    fell = [False for _ in range(len(blocks))]
    while count != 0:
        count = 0
        ground = False
        for i in range(len(cblocks)):
            b = cblocks[i]
            for el in b:
                if el[2] <= lowest:
                    ground = True
                    break
            if ground:
                ground = False
                continue
            for el in b:
                cgame[el[0]][el[1]][el[2]] = '0'
                el[2] -= 1
            if intersect(cgame, b):
                for el in b:
                    el[2] += 1
                    cgame[el[0]][el[1]][el[2]] = 'B'
            else:
                fell[i] = True
                count += 1
                for el in b:
                    cgame[el[0]][el[1]][el[2]] = 'B'
    total += sum(fell)
    print(total)
    for el in block:
        game[el[0]][el[1]][el[2]] = 'B'
        
print(total) 