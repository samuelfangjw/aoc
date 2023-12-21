import sys
import math
import numpy as np
from collections import defaultdict, deque

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
grid = []

with open(file) as f:
    for line in f:
        line = line.strip()
        grid.append(line)

R,C = len(grid),len(grid[0])
for r in range(R):
    for c in range(C):
        if grid[r][c] == 'S':
            S = (r,c)
            break

dirs = [(0,1), (0,-1), (1,0), (-1,0)]

pts = defaultdict(int)
seen = set()
part1 = 0
target1 = 64
target2 = 26501365

q = deque()
q.append((S, 0))
while q:
    (r,c), steps = q.popleft()

    if (r,c, steps) in seen:
        continue
    seen.add((r,c,steps))

    if steps == R * 2 + (target2 % R) + 1:
        break

    if steps % R == target2 % R:
        pts[steps] += 1
    
    if steps == target1:
        part1 += 1

    for dr,dc in dirs:
        nr,nc = r+dr,c+dc
        if grid[nr%R][nc%C] != '#':
            q.append(((nr,nc), steps+1))

ys = list(pts.values())
f = np.polyfit([0,1,2],ys,2)
x = target2 // R
part2 = math.ceil(f[0]*x**2 + f[1]*x + f[2])

print(part1, part2)
