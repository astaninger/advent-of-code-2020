#!/usr/bin/env python

import sys, itertools, collections

arr = []
for line in sys.stdin:
    arr.append(int(line.strip()))

# with open("input.txt") as file:
#     inp = file.read().strip()
one = 0
three = 1
last = 0
for line in sorted(arr):
    if line - last == 3:
        three += 1
    elif line - last == 1:
        one += 1
    last = line
print(one*three)

'''
1 4 5 6 7
1 1 1 2 3
'''
seen = set(arr)
seen.add(max(arr)+3)
dp = [0]*(max(arr)+4)
dp[0] = 1
arr.append(0)
for line in sorted(arr):
    for off in 1,2,3:
        if line+off in seen:
            dp[line+off] += dp[line]
print(dp[-1])
