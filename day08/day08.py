#!/usr/bin/env python

import sys, itertools, collections

arr = []
for line in sys.stdin:
    arr.append(line.strip())å

i = 0
acc = 0
seen = set()
while i < len(arr) and i not in seen:
	cmd, val = arr[i].split()
	val = int(val)
	seen.add(i)
	if cmd == 'acc':
		acc += val
		i+=1
	elif cmd == 'jmp':
		i += val
	else:
		i+=1
print(acc)

i = 0
tried = set()
jmpTried= set()
while i != len(arr):
	used = False
	seen = set()
	acc = 0
	i=0
	while i < len(arr) and i not in seen:
		cmd, val = arr[i].split()
		val = int(val)
		seen.add(i)
		if cmd == 'acc':
			acc += val
			i+=1
		elif cmd == 'jmp':
			if not used and i not in jmpTried:
				used = True
				jmpTried.add(i)
				i += 1
			else:
				i += val
		else:
			if not used and i not in tried:
				used = True
				tried.add(i)
				i += val
			else:
				i+=1
print(acc)
