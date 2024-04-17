# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 20:13:04 2023

@author: Peyton Daley
"""
def test_game(given, game):
    for i in range(int(len(game)/2)):
        num = int(game[2*i])
        color = game[2*i+1].replace(',', '')
        if num > given[color]:
            return False
    return True

given = dict()
given['red'] = 12
given['blue'] = 14
given['green'] = 13
total = 0

f = open("input.txt")
for x in f:
    test = True
    game_num = x.split()[1]
    game_num = int(game_num[:len(game_num)-1])
    game = x[6 + len(str(game_num)):]
    games = game.split(';')
    games = [x.split() for x in games]
    for game in games:
        test = test and test_game(given, game)
    if test:
        total += game_num
   
print(total)