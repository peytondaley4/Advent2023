# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 00:00:25 2023

@author: Peyton Daley
"""

f = open("input.txt")

sum_ = 0

data = f.read().split('\n')
data = data[:len(data)-1]

num_cards = [1] * len(data)

for line in data:
    card_num = line.split()[1]
    card_num = int(card_num[:len(card_num)-1])
    game = line.split(':')[1]
    nums = game.split('|')
    win_nums = nums[0].split()
    your_nums = nums[1].split()
    total = 0
    for num in your_nums:
        if num in win_nums:
            total += 1
    for i in range(total):
        num_cards[card_num + i] += num_cards[card_num-1]

print(num_cards)
print(sum(num_cards))