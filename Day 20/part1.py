# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 17:50:51 2023

@author: Peyton Daley
"""
f = open('input.txt')
modules = dict()
for line in f:
    name = line.split(' -> ')[0]
    vals = line.strip().split(' -> ')[1].split(', ')
    if name[0] == 'b':
        modules[name] = [0, vals]
    elif name[0] == '%':
        modules[name[1:]] = [1, 0, vals]
    else:
        modules[name[1:]] = [2, dict(), vals]
        
for en in modules:
    val = modules[en]
    if val[0] == 2:
        for en2 in modules:
            val2 = modules[en2]
            if val2[0] == 0 and en in val2[1]:
                val[1][en2] = 'low'
            elif val2[0] != 0 and en in val2[2]:
                val[1][en2] = 'low'
rx_count = 0
presses = 0
while rx_count != 1:
    rx_count = 0
    presses += 1
    pulses = [('broadcaster', 'low')]
    while len(pulses) != 0:
        rem_pulse = []
        pulse = pulses[0]
        if pulse[0] == 'rx':
            if pulse[1] == 'low':
                print('here')
                rx_count += 1
            pulses.remove(pulse)
            continue
        if modules[pulse[0]][0] == 0:
            for i in modules[pulse[0]][1]:
                pulses.append((i, pulse[1], pulse[0]))
        elif modules[pulse[0]][0] == 1 and pulse[1] == 'low':
            val = modules[pulse[0]]
            if val[1]:
                for i in val[2]:
                    pulses.append((i, 'low', pulse[0]))
            else:
                for i in val[2]:
                    pulses.append((i, 'high', pulse[0]))
            val[1] = not val[1]
        elif modules[pulse[0]][0] == 2:
            val = modules[pulse[0]]
            val[1][pulse[2]] = pulse[1]
            all_high = True
            if pulse[0] == 'gf' and 'high' in val[1].values():
                print(val[1], presses)
            for mod in val[1]:
                if val[1][mod] == 'low':
                    all_high = False
                    continue
            for i in val[2]:
                if all_high:
                    pulses.append((i, 'low', pulse[0]))
                else:
                    pulses.append((i, 'high', pulse[0]))
        pulses.remove(pulse)
print(presses)