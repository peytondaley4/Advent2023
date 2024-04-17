# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 09:41:16 2023

@author: Peyton Daley
"""
def intersect_plane(line, plane):
    t = (plane[3] - plane[0] * line[0][0] - plane[1] * line[0][1] - plane[2] * line[0][2])
    d = (plane[0] * line[1][0] + plane[1] * line[1][1] + plane[2] * line[1][2])
    return find_point(line, t / d)

def cross(v1, v2):
    x = v1[1] * v2[2] - v1[2] * v2[1]
    y = v1[2] * v2[0] - v1[0] * v2[2]
    z = v1[0] * v2[1] - v1[1] * v2[0]
    return (x,y,z)
    
def find_point(line, t):
    x = line[0][0] + line[1][0] * t
    y = line[0][1] + line[1][1] * t
    z = line[0][2] + line[1][2] * t
    return (x,y,z)

def make_line(p1, p2):
    vx = (p1[0] - p2[0])
    vy = (p1[1] - p2[1])
    vz = (p1[2] - p2[2])
    return((p1, (vx,vy,vz)))

def intersect(l1, l2):
    pos1, pos2 = l1[0], l2[0]
    vel1, vel2 = l1[1], l2[1]
    top = vel1[0] * vel2[0] * pos2[1] - vel1[0] * vel2[0] * pos1[1] + vel2[0] * vel1[1] * pos1[0] - vel1[0] * vel2[1] * pos2[0]
    bottom = vel2[0] * vel1[1] - vel2[1] * vel1[0]
    int_x = top / bottom
    t1 = (int_x - pos1[0]) / vel1[0]
    t2 = (int_x - pos2[0]) / vel2[0]
    print(t1, t2)
    print(find_point(l1, t1), find_point(l2, t2))
    if find_point(l1, t1) != find_point(l2, t2):
        return find_point(l1, t1), t1
    return False

def plane(line, line2, point):
    p1 = find_point(line, 0)
    p2 = find_point(line, 1)
    v1 = (p1[0] - p2[0], p1[1] - p2[1], p1[2] - p2[2])
    v2 = ((p1[0] - point[0], p1[1] - point[1], p1[2] - point[2]))
    n = cross(v1, v2)
    d = n[0] * point[0] + n[1] * point[1] + n[2] * point[2]
    p1 = intersect_plane(line2, (n[0], n[1], n[2], d))
    return make_line(p1, point)

f = open('input3.txt')
stones = []
for line in f:
    pos = list(int(x) for x in line.split('@')[0].split(', '))
    vel = list(int(x) for x in line.split('@')[1].split(', '))
    stones.append((pos, vel))
    

l1 = plane(stones[0], stones[1], find_point(stones[2], 0))
l2 = plane(stones[0], stones[1], find_point(stones[2], 15))
point = find_point(l1, 0)
i, _ = intersect(l1, l2)
print(i)
n = cross(l1[1], l2[1])
d = n[0] * point[0] + n[1] * point[1] + n[2] * point[2]
line = make_line(intersect_plane(stones[3], (n[0], n[1], n[2], d)), i)
_, t1 = intersect(stones[0], line)
_, t2 = intersect(stones[1], line)
p1 = find_point(stones[0], t1)
p2 = find_point(stones[1], t2)
Vx = (p2[0] - p1[0]) / (t2-t1)
fac = Vx / line[1][0]
line = (line[0], (line[1][0] * fac, line[1][1] * fac, line[1][2] * fac))
line = ((p1[0] - line[1][0] * t1, p1[1] - line[1][1]*t1, p1[2] - line[1][2]*t1), line[1])
print(line)
print(intersect(line, stones[1]))
print(sum(line[0]))