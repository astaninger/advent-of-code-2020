#!/usr/bin/env python

import sys, itertools, collections

arr = []
for line in sys.stdin:
    arr.append(line.strip())

res = 0
x = 0
for line in arr:
	if line[x % len(line)] == '#':
		res += 1
	x += 3
print(res)

res2 = [0,0, 0, 0]
loc = [0, 0, 0, 0]
slope = [1, 3, 5, 7]
for line in arr:
	for i in range(len(loc)):
		if line[loc[i] % len(line)] == '#':
			res2[i] += 1
		loc[i] += slope[i]
x = 0
res3 = 0
for a in range(0, len(arr), 2):
	if arr[a][x % len(arr[a])] == '#':
		res3 += 1
	x += 1
b = 1
for num in res2:
	b *= num
b*=res3
print(b)
