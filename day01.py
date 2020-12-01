#!/usr/bin/env python

import sys, itertools, collections
seen = set()
for line in sys.stdin:
	curr = int(line.strip())
	if 2020 - curr in seen:
		print(curr * (2020 - curr))
		break
	seen.add(curr)

nums = list(seen)
for i in range(len(nums)-2):
	for j in range(i + 1, len(nums)-1):
		for k in range(j + 1, len(nums)):
			if nums[i] + nums[k] + nums[j] == 2020:
				print(nums[i] * nums[j] * nums[k])
				quit()