#!/usr/bin/env python

import sys, itertools, collections

arr = []
for line in sys.stdin:
    arr.append(line.strip())

# with open("input.txt") as file:
#     inp = file.read().strip()
curZeroMask = 0
curOneMask = 0
memory= {}
for line in arr:
    if line.startswith('mask'):
        curZeroMask = int(line[7:].replace('X', '0'), 2)
        curOneMask = int(line[7:].replace('X', '1'), 2)
    else:
        a, b = line.split('=')
        c = a.find(']')
        a = a[4:c]
        memory[a] = (int(b) & curOneMask) | curZeroMask

print(sum(memory.values()))

curZeroMask = 0
curMask = 0
perms = []
memory= {}
for line in arr:
    if line.startswith('mask'):
        xCount = line[7:].count('X')
        perms = [ bin(x)[2:].zfill(xCount) for x in range(0, 2**xCount)]
        curZeroMask = int(line[7:].replace('X', '0'), 2)
        curMask = line[7:]
    else:
        a, b = line.split('=')
        c = a.find(']')
        a = int(a[4:c]) | curZeroMask
        aBin = list(bin(a)[2:].zfill(len(curMask)))
        # print(aBin)
        for p in perms:
            j = 0
            curBin = aBin
            for i in range(len(curMask)):
                if curMask[i] == 'X':
                    curBin[i] = p[j]
                    j += 1
            # print('curBin', )
            memory[int(''.join(curBin), 2)] = int(b)
# print(memory)
print(sum(memory.values()))
