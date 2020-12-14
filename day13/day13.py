#!/usr/bin/env python

from sys import *
from functools import *
from collections import *

arr = []
for line in sys.stdin:
    arr.append(line.strip())

# with open(sys.stdin) as file:
#     inp = file.read().strip()
time = int(arr[0])
buses = arr[1].split(',')
minWaitTime = float('inf')
minWaitBus = -1
for bus in buses:
    if bus != 'x':
        print(time // int(bus))
        if ((time // int(bus)) + 1)*int(bus) < minWaitTime:
            minWaitTime = ((time // int(bus)) + 1)*int(bus)
            minWaitBus = int(bus)

print(minWaitBus*(minWaitTime - time))
offSet = []
'''
7x = y
13x - 1 = y
59x - 2 = y
'''
for i, bus in enumerate(buses):
    if bus != 'x':
        offSet.append([i, bus])

t = 0
prod = 1
for off, a in offSet:
    while (t + off) % int(a) != 0:
        t += prod
    prod*=int(a)
print(t)
