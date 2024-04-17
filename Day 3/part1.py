# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 15:53:57 2023

@author: Peyton Daley
"""

def get_num(row, col, cols, data):
    num = data[row][col]
    data[row][col] = '.'
    left = col - 1
    right = col + 1
    while (left >= 0 and data[row][left].isdigit()):
        num = data[row][left] + num
        data[row][left] = '.'
        left -= 1
    while (right < cols and data[row][right].isdigit()):
        num = num + data[row][right]
        data[row][right] = '.'
        right += 1
    return int(num)

def get_nums_around(row,col,data):
    nums = []
    num_rows = len(data)
    num_cols = len(data[0])
    if (row > 0 and data[row-1][col].isdigit()):
        nums.append(get_num(row-1, col, num_cols, data))
    if (row < num_rows - 1 and data[row+1][col].isdigit()):
        nums.append(get_num(row+1, col, num_cols, data))
    if (col > 0 and data[row][col-1].isdigit()):
        nums.append(get_num(row, col-1, num_cols, data))
    if (col < num_cols - 1 and data[row][col+1].isdigit()):
        nums.append(get_num(row, col+1, num_cols, data))
    if (row > 0 and col > 0 and data[row-1][col-1].isdigit()):
        nums.append(get_num(row-1, col-1, num_cols, data))
    if (row > 0 and col < num_cols - 1 and data[row-1][col+1].isdigit()):
        nums.append(get_num(row-1, col+1, num_cols, data))
    if (row < num_rows - 1 and col > 0 and data[row+1][col-1].isdigit()):
        nums.append(get_num(row+1, col-1, num_cols, data))
    if (row < num_rows - 1 and col < num_cols - 1 and data[row+1][col+1].isdigit()):
        nums.append(get_num(row+1, col+1, num_cols, data))
    return nums

def get_total(data):
    total = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if (not data[i][j].isdigit() and not data[i][j] == '.'):
                sum_ = sum(get_nums_around(i,j,data))
                print(sum_)
                total += sum_
    return total

f = open('input.txt')

data = []

for line in f:
    data.append(list(line.strip()))

print(get_total(data))