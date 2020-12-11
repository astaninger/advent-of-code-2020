#!/usr/bin/env python

import sys, itertools, collections
from collections import defaultdict
arr = []
for line in sys.stdin:
    arr.append(list(line.strip()))

# with open("input.txt") as file:
#     inp = file.read().strip()
changed = True
while changed:
    changed = False
    tohash = []
    toL = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 'L':
                for x, y in [[i-1, j], [i - 1, j -1, ], [i-1,j+1], [i, j+1], [i, j-1], [i+1, j-1], [i+1, j], [i+1, j+1]]:
                    if 0 <= x < len(arr) and 0 <= y < len(arr[0]) and arr[x][y] == '#':
                        break
                else:
                    changed = True
                    tohash.append([i, j])
            elif arr[i][j] == '#':
                count = 0
                for x, y in [[i-1, j], [i - 1, j -1, ], [i-1,j+1], [i, j+1], [i, j-1], [i+1, j-1], [i+1, j], [i+1, j+1]]:
                    if 0 <= x < len(arr) and 0 <= y < len(arr[0]) and arr[x][y] == '#':
                        count += 1
                if count >= 4:
                    changed = True
                    toL.append([i, j])
    # print(arr)
    for i, j in tohash:
        arr[i][j] = '#'
    for i, j in toL:
        arr[i][j] = 'L'
ans = 0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == '#':
            ans += 1
print(ans)


changed = True
while changed:
    changed = False
    tohash = []
    toL = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 'L':
                x, y = i-1, j-1
                while 0 <= x < len(arr) and 0 <= y < len(arr[0]) and arr[x][y] == '.':
                    x -= 1
                    y -= 1
                if x < 0 or x == len(arr) or y< 0 or y == len(arr[0]) or arr[x][y] == 'L':
                    pass
                else:
                    continue

                x, y = i-1, j
                while 0 <= x < len(arr) and 0 <= y < len(arr[0]) and arr[x][y] == '.':
                    x -= 1
                if x < 0 or x == len(arr) or y< 0 or y == len(arr[0])or arr[x][y] == 'L':
                    pass
                else:
                    continue

                x, y = i-1, j+1
                while 0 <= x < len(arr) and 0 <= y < len(arr[0]) and arr[x][y] == '.':
                    x -= 1
                    y+=1
                if x < 0 or x == len(arr) or y < 0 or y == len(arr[0])or arr[x][y] == 'L':
                    pass
                else:
                    continue

                x, y = i, j-1
                while 0 <= x < len(arr) and 0 <= y < len(arr[0]) and arr[x][y] == '.':
                    y -= 1
                if x < 0 or x == len(arr) or y <0 or y == len(arr[0]) or arr[x][y] == 'L':
                    pass
                else:
                    continue

                x, y = i, j+1
                while 0 <= x < len(arr) and 0 <= y < len(arr[0]) and arr[x][y] == '.':
                    y += 1
                if x < 0 or x == len(arr) or y < 0 or y == len(arr[0]) or arr[x][y] == 'L':
                    pass
                else:
                    continue

                x, y = i+1, j+1
                while 0 <= x < len(arr) and 0 <= y < len(arr[0]) and arr[x][y] == '.':
                    x += 1
                    y += 1
                if x < 0 or x == len(arr) or y < 0 or y == len(arr[0]) or arr[x][y] == 'L':
                    pass
                else:
                    continue


                x, y = i+1, j
                while 0 <= x < len(arr) and 0 <= y < len(arr[0]) and arr[x][y] == '.':
                    x += 1

                if x < 0 or x == len(arr) or y < 0 or y == len(arr[0]) or arr[x][y] == 'L':
                    pass
                else:
                    continue

                x, y = i+1, j-1
                while 0 <= x < len(arr) and 0 <= y < len(arr[0]) and arr[x][y] == '.':
                    x += 1
                    y-=1
                if x < 0 or x == len(arr) or y < 0 or y == len(arr[0]) or arr[x][y] == 'L':
                    pass
                else:
                    continue

                changed = True
                tohash.append([i, j])
            elif arr[i][j] == '#':
                count = 0
                x, y = i-1, j-1
                while 0 <= x < len(arr) and 0 <= y < len(arr[0]) and arr[x][y] == '.':
                    x -= 1
                    y -= 1
                if x < 0 or x == len(arr) or y < 0 or y == len(arr[0]) or arr[x][y] == 'L':
                    pass
                else:
                    # print(x, y)
                    count += 1

                x, y = i-1, j
                while 0 <= x < len(arr) and 0 <= y < len(arr[0]) and arr[x][y] == '.':
                    x -= 1
                if x < 0 or x == len(arr) or y < 0 or y == len(arr[0]) or arr[x][y] == 'L':
                    pass
                else:
                    count += 1

                x, y = i-1, j+1
                while 0 <= x < len(arr) and 0 <= y < len(arr[0]) and arr[x][y] == '.':
                    x -= 1
                    y+=1
                if x < 0 or x == len(arr) or y < 0 or y == len(arr[0]) or arr[x][y] == 'L':
                    pass
                else:
                    count += 1

                x, y = i, j-1
                while 0 <= x < len(arr) and 0 <= y < len(arr[0]) and arr[x][y] == '.':
                    y -= 1
                if x < 0 or x == len(arr) or y < 0 or y == len(arr[0]) or arr[x][y] == 'L':
                    pass
                else:
                    count += 1

                x, y = i, j+1
                while 0 <= x < len(arr) and 0 <= y < len(arr[0]) and arr[x][y] == '.':
                    y += 1
                if x < 0 or x == len(arr) or y < 0 or y == len(arr[0]) or arr[x][y] == 'L':
                    pass
                else:
                    count += 1

                x, y = i+1, j+1
                while 0 <= x < len(arr) and 0 <= y < len(arr[0]) and arr[x][y] == '.':
                    x += 1
                    y += 1
                if x < 0 or x == len(arr) or y < 0 or y == len(arr[0]) or arr[x][y] == 'L':
                    pass
                else:
                    count += 1


                x, y = i+1, j
                while 0 <= x < len(arr) and 0 <= y < len(arr[0]) and arr[x][y] == '.':
                    x += 1

                if x < 0 or x == len(arr) or y < 0 or y == len(arr[0]) or arr[x][y] == 'L':
                    pass
                else:
                    count += 1

                x, y = i+1, j-1
                while 0 <= x < len(arr) and 0 <= y < len(arr[0]) and arr[x][y] == '.':
                    x += 1
                    y-=1
                if x < 0 or x == len(arr) or y <  0 or y == len(arr[0]) or arr[x][y] == 'L':
                    pass
                else:
                    count += 1
                # print(count)
                if count >= 5:
                    changed = True
                    toL.append([i, j])
    # print('L', toL)
    # print('HAHS', tohash)
    for i, j in tohash:
        arr[i][j] = '#'
    for i, j in toL:
        arr[i][j] = 'L'
    # for line in arr:
    #     print(line)
    # print('----')
ans = 0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == '#':
            ans += 1
print(ans)
