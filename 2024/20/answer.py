import sys
from collections import deque

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    grid = []
    for line in f:
        line = line.strip()
        grid.append(list(line))

R, C = len(grid), len(grid[0])
for i, j in [(i, j) for i in range(R) for j in range(C)]:
    if grid[i][j] == 'S':
        start = (i, j)
    if grid[i][j] == 'E':
        goal = (i, j)

def manhatten(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

dist_from_goal = {}

q = deque([(goal, 0)])

while q:
    (r, c), steps = q.popleft()

    if grid[r][c] == '#':
        continue
    
    if (r, c) in dist_from_goal:
        continue

    dist_from_goal[(r, c)] = steps

    for nr, nc in [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]:
        q.append(((nr, nc), steps+1))

def solve(d):
    count = 0

    for i, j in dist_from_goal.keys():
        for a, b in dist_from_goal.keys():
            if (i, j) == (a, b):
                continue

            if (dist := manhatten((i, j), (a, b))) > d:
                continue
            
            if dist_from_goal[(i,j)] - dist_from_goal[(a,b)] - dist >= 100:
                count += 1

    return count

print("Part 1:", solve(2))
print("Part 2:", solve(20))
