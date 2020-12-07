#!/usr/bin/env python

import sys, itertools, collections

arr = []
for line in sys.stdin:
    arr.append(line.strip())

ans = float('-inf')
# arr = ['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL', 'BBBBBBBRRR']
seen = [[0 for _ in range(8)] for _ in range(128)]
for line in arr:
	# line = 'BFFFBBFRRR'
	row = line[:7]
	col = line[7:]
	l1 = 0
	r = 127
	i = 0
	for i in range(7):
		mi1 = (l1 + r) // 2
		if row[i] == 'F':
			r = mi1
		else:
			l1 = mi1 + 1
	l = 0
	r = 7

	for i in range(3):
		mi2 = (l + r) // 2
		if col[i] == 'L':
			r = mi2
		else:
			l = mi2 + 1

	seen[l1][l] = ((l1*8)+l)
	ans = max(ans, (l1*8)+l)

print(ans)
print(seen)
