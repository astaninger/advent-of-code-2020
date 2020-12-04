#!/usr/bin/env python

import sys, itertools, collections

arr = []
count = 0
for line in sys.stdin:
	arr.append(line)
a = "".join(arr)
print(a.split('\n\n')[0].split())
ds = []
countb = 0
for i, line in enumerate(a.split('\n\n')):
	ds.append(dict())
	for s in line.split():
		k, v = s.split(':')
		ds[i][k] = v
	if 'byr' in ds[i] and 'iyr' in ds[i] and 'eyr' in ds[i] and 'hgt' in ds[i] and 'hcl' in ds[i] and 'ecl' in ds[i] and 'pid' in ds[i]:
		count += 1
		if 1920 <= int(ds[i]['byr']) <= 2002 and 2010 <= int(ds[i]['iyr']) <= 2020 and 2020 <= int(ds[i]['eyr']) <= 2030:
				hgt = ds[i]['hgt']
				if (hgt[-2:] == 'in' and 59 <= int(hgt[:-2]) <= 76) or (hgt[-2:] == 'cm' and 150 <= int(hgt[:-2]) <= 193):
					hcl = ds[i]['hcl']
					if hcl[0] == '#' and len(hcl[1:]) == 6 and hcl[1:].isalnum:
						if ds[i]['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
							if len(ds[i]['pid']) == 9 and ds[i]['pid'].isdigit:
								countb +=1
print(count)
print(countb)
