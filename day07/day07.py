#!/usr/bin/env python

import sys, itertools, collections

arr = []
for line in sys.stdin:
	arr.append(line)

reversegraph = collections.defaultdict(list)
graph = collections.defaultdict(list)
bagCount = collections.Counter()
for line in arr:
	a, b = line.strip().split('contain')
	h, i, j = a.split()
	c = b.strip().split(', ')
	for s in c:
		if s == 'no other bags.':
			continue
		d, e, f, g = s.split()
		reversegraph[e + f].append(h+i)
		graph[h+i].append((e+f, int(d)))
ans = set()
def dfs(node):
	for nei in reversegraph[node]:
		ans.add(nei)
		dfs(nei)
dfs('shinygold')
print(len(ans))

def dfs2(node, mult):
	count = 0
	for nei, num in graph[node]:
		count += mult*num
		count += dfs2(nei, mult*num)
	return count

ans1 = dfs2('shinygold', 1)
print(ans1)

