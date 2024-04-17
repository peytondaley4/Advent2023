# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 14:51:01 2023

@author: Peyton Daley
"""
from collections import deque

def rem_edge(nodes, edge):
    n1 = edge[0]
    n2 = edge[1]
    nodes[n1].remove(n2)
    nodes[n2].remove(n1)
    
def add_edge(nodes, edge):
    n1 = edge[0]
    n2 = edge[1]
    nodes[n1].add(n2)
    nodes[n2].add(n1)

def bfs(nodes, start):
    ns = deque()
    ns.append(start)
    visited = set()
    visited.add(start)
    while len(ns) != 0:
        n = ns.popleft()
        for i in nodes[n]:
            if i not in visited:
                ns.append(i)
                visited.add(i)
    return visited

f = open('input.txt')
nodes = dict()
for line in f:
    name = line.split(': ')[0]
    ns = line.split(': ')[1].strip().split()
    if name not in nodes:
        nodes[name] = set()
    nodes[name] = nodes[name].union(set(ns))
    for n in ns:
        if n in nodes:
            nodes[n].add(name)
        else:
            nodes[n] = set([name])

edges = []
for n in nodes:
    for n2 in nodes[n]:
        if (n2, n) not in edges:
            edges.append((n, n2))
            
for i in range(len(edges)-2):
    print(i, len(edges))
    rem_edge(nodes, edges[i])
    for j in range(i+1,len(edges)-1):
        rem_edge(nodes, edges[j])
        print(j)
        for k in range(j+1, len(edges)):
            rem_edge(nodes, edges[k])
            l = bfs(nodes, 'lhk')
            add_edge(nodes, edges[k])
            if len(l) == len(nodes):
                continue
            o = set(nodes.keys()).difference(l)
            print(edges[i], edges[j], edges[k])
            print(o, l, len(o) * len(l))
        add_edge(nodes, edges[j])
    add_edge(nodes, edges[i])
            
print(len(edges))