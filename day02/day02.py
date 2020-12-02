#!/usr/bin/env python

import sys, itertools, collections
arr = []
for line in sys.stdin:
	arr.append(line.strip())

count = 0
for line in arr:
	a, b, c = line.split()
	first, end = a.split('-')
	counts = collections.Counter(c)
	if int(first) <= counts[b[0]] <= int(end):
		count += 1

print(count)

count = 0
for line in arr:
	line = line.strip()
	a, b, c = line.split()
	first, end = a.split('-')
	b = b[0]
	if (c[int(first)-1] == b and c[int(end)-1] != b) or (c[int(first)-1] != b and c[int(end)-1] == b):
		count += 1

print(count)
