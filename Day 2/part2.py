# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 20:13:04 2023

@author: Peyton Daley
"""
def get_min(games):
    values = dict()
    for game in games:
        for i in range(int(len(game) / 2)):
            num = int(game[2*i])
            color = game[2*i+1].replace(',', '').strip()
            if color not in values:
                values[color] = num
            if num > values[color]:
                values[color] = num
    return values

total = 0

f = open("input.txt")
for x in f:
    game_num = x.split()[1]
    game_num = int(game_num[:len(game_num)-1])
    game = x[6 + len(str(game_num)):]
    games = game.split(';')
    games = [x.split() for x in games]
    final = get_min(games)
    tot = 1
    for key in final.keys():
        tot *= final[key]
    total += tot

print(total)