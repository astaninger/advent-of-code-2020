#!/usr/bin/env python

import sys, itertools, collections, string

arr = []
for line in sys.stdin:
    arr.append(line.strip())
ans = []
curr = set()
for l in arr:
	if l == '':
		ans.append(curr)
		curr = set()
	else:
		curr |= set(l)
ans.append(curr)
print(sum(len(s) for s in ans))

ans = 0
currCount = 0
curr = collections.Counter()
for l in arr:
	if l == '':
		for c in curr.keys():
			if curr[c] == currCount:
				ans += 1
		currCount = 0
		curr = collections.Counter()
	else:
		currCount += 1
		curr += collections.Counter(l)
for c in string.ascii_lowercase:
	if curr[c] == currCount:
		ans += 1

print(ans)
