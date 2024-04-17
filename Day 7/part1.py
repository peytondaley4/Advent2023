# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 11:20:53 2023

@author: Peyton Daley
"""
def hand_to_num(hand):
    e = pow(13, 4)
    res = 0
    for num in hand:
        if num == 'A':
            res += e * 12
        elif num == 'K':
            res += e * 11
        elif num == 'Q':
            res += e * 10
        elif num == 'J':
            res += 0
        elif num == 'T':
            res += e * 9
        else:
            res += e * (int(num) - 1)
        e = e / 13
    return res

def rank_hand(hand):
    if len(set(hand)) == 1:
        return 7
    if len(set(hand)) == 2:
        hand_set = set(hand)
        elem = hand_set.pop()
        if hand.count(elem) == 1 or hand.count(elem) == 4:
            return 6
        else:
            return 5
    if len(set(hand)) == 3:
        hand_set = set(hand)
        for elem in hand_set:
            if hand.count(elem) == 3:
                return 4
        return 3
    if len(set(hand)) == 4:
        return 2
    return 1

def jokers(hand):
    alts = []
    chars = ['A','K','Q','T','9','8','7','6','5','4','3','2']
    for i in range(len(hand)):
        if hand[i] == 'J':
            for char in chars:
                if char not in hand:
                    continue
                alts.append(hand[:i] + char + hand[i+1:])
    for alt in alts:
        alts += jokers(alt)
    return list(set(alts))

f = open('input.txt')

cards = []
prizes = []
ranks = []

for line in f:
    cards.append(line.split()[0])
    prizes.append(line.split()[1])
    
for i in range(len(cards)):
    alts = jokers(cards[i])
    alts.append(cards[i])
    rank = max(rank_hand(x) for x in alts)
    ranks.append((rank, hand_to_num(cards[i]), prizes[i], cards[i]))
    
ranks.sort(reverse = True)
print(ranks)

rank = len(ranks)
total = 0
for r in ranks:
    total += rank * int(r[2])
    rank -= 1
    
print(total)