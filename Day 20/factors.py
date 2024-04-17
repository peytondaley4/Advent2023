# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 19:47:34 2023

@author: Peyton Daley
"""
num = 5040
for i in range(1, int(num ** 0.5)+1):
    if num % i == 0:
        print(i, num // i)