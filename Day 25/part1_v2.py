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

def bfs(nodes, start, edges, edge_count):
    ns = deque()
    ns.append(start)
    visited = set()
    visited.add(start)
    while len(ns) != 0:
        n = ns.popleft()
        for i in nodes[n]:
            if i not in visited:
                if (n, i) in edges:
                    edge_count[edges.index((n,i))] += 1
                else:
                    edge_count[edges.index((i,n))] += 1
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
            
edge_count = [0] * len(edges)
count = 0
for n in nodes:
    print(count, len(nodes))
    bfs(nodes, n, edges, edge_count)
    count += 1
            
s = sorted(edge_count, reverse = True)[:3]
for i in s:
    rem_edge(nodes, edges[edge_count.index(i)])
l = bfs(nodes, 'bcf', edges, edge_count)
    
print(len(set(nodes.keys()).difference(l)) * len(l))