#!/usr/bin/env python

import sys, itertools, collections

arr = []
for line in sys.stdin:
    arr.append(int(line.strip()))

s = collections.Counter(arr[:25])
l = 0

for r in range(25, len(arr)):
    for c in s.keys():
        if s[c] == 0: continue
        if arr[r] - c != c and arr[r] - c in s and s[arr[r] - c] > 0:
            break
    else:
        print(arr[r])
        break
    s[arr[l]] -= 1
    l += 1
    s[arr[r]] += 1

ans1 = arr[r]
l = 0
curr = 0

for r in range(ans1):
	curr += arr[r]

	while l < r and curr > ans1:
		curr -= arr[l]
		l+=1
	if curr == ans1:
		break
print(min(arr[l:r]) + max(arr[l:r]))
