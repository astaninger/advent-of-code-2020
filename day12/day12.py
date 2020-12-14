#!/usr/bin/env python

import sys, itertools, collections

arr = []
for line in sys.stdin:
    arr.append(line.strip())

# with open("input.txt") as file:
#     inp = file.read().strip()
x, y = 0, 0
dir = 0
dirs = {0: 'E', 90: 'N', 180: 'W', 270: 'S'}
for line in arr:
    a, b = line[0], line[1:]
    b = int(b)
    if a == 'F':
        a = dirs[dir]
    if a == 'N':
        y += b
    elif a == 'E':
        x += b
    elif a == 'S':
        y -= b
    elif a == 'W':
        x -= b
    elif a == 'L':
        dir += b
        dir %= 360
    elif a == 'R':
        dir -= b
        dir %= 360
print(abs(x) + abs(y))

wayX, wayY = 10, 1
x, y = 0, 0
dir = 0
dirs = {0: 'E', 90: 'N', 180: 'W', 270: 'S'}
for line in arr:
    a, b = line[0], line[1:]
    b = int(b)
    if a == 'F':
        c = dirs[dir]
        if c == 'N':
            y += wayX*b
            x -= wayY*b
        elif c == 'E':
            x += wayX*b
            y += wayY*b
        elif c == 'S':
            y -= wayX*b
            x += wayY*b
        elif c == 'W':
            x -= wayX*b
            y -= wayY*b
    elif a == 'N':
        c = dirs[dir]
        if c == 'N':
            wayX += b
        elif c == 'E':
            wayY += b
        elif c == 'S':
            wayX -= b
        elif c == 'W':
            wayY -= b
    elif a == 'E':
        c = dirs[dir]
        if c == 'N':
            wayY -= b
        elif c == 'E':
            wayX += b
        elif c == 'S':
            wayY += b
        elif c == 'W':
            wayX -= b
    elif a == 'S':
        c = dirs[dir]
        if c == 'N':
            wayX -= b
        elif c == 'E':
            wayY -= b
        elif c == 'S':
            wayX += b
        elif c == 'W':
            wayY += b
    elif a == 'W':
        c = dirs[dir]
        if c == 'N':
            wayY += b
        elif c == 'E':
            wayX -= b
        elif c == 'S':
            wayY -= b
        elif c == 'W':
            wayX += b
    elif a == 'L':
        dir += b
        dir %= 360
    elif a == 'R':
        dir -= b
        dir %= 360

    print(x, y, wayX, wayY, dirs[dir])
print(abs(x) + abs(y))
