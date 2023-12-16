import sys
import math
from collections import deque

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    grid = []
    for line in f:
        line = list(line.strip())
        grid.append(line)

R, C = len(grid), len(grid[0])
for r in range(R):
    for c in range(C):
        if grid[r][c] == "S":
            S = (r, c)

dirs = [(0,1), (0,-1), (1,0), (-1,0)]

###### PART 1 #######

pipes = {
    # N: (-1,0), S: (1,0), E:(0,1), W:(0,-1)
    "|": {
        (1,0): (1,0), # if enter | pipe with (1,0), exit | pipe with (1,0)
        (-1,0): (-1,0)
    },
    "-": {
        (0,1): (0,1),
        (0,-1): (0,-1)
    },
    "L": {
        (1,0): (0,1),
        (0,-1): (-1,0)
    },
    "J": {
        (1,0): (0,-1),
        (0,1): (-1,0)
    },
    "7": {
        (-1,0): (0,-1),
        (0,1): (1,0)
    },
    "F": {
        (-1,0): (0,1),
        (0,-1): (1,0)
    },
}

# (row, col, dir travelled, path from start)
q = deque([(S[0]+dr, S[1]+dc, (dr,dc), [(dr,dc)]) for dr,dc in dirs])
while q:
    row, col, dir, path = q.popleft()

    if row < 0 or row >= R or col < 0 or col >= C:
        continue

    if grid[row][col] == "S":
        cycle = path
        part1 = math.ceil(len(path) / 2) # furthest point is half distance of loop
        break

    next_dir = pipes.get(grid[row][col], {}).get(dir, {})
    if next_dir:
        new_path = [x for x in path]
        new_path.append(next_dir)
        q.append((row+next_dir[0], col+next_dir[1], (next_dir), new_path))

###### PART 2 #######

# expand grid by 2X. Mark only the cycle with X.
grid2 = [["1" for _ in range(C * 2)] for _ in range(R * 2)]

row, col = S[0]*2, S[1]*2

for dr, dc in cycle:
    row += dr
    col += dc
    grid2[row][col] = "X"
    row += dr
    col += dc
    grid2[row][col] = "X"

R2, C2 = R*2, C*2

# flood fill from outside
q = deque([(R2-1, C2-1)])

while q:
    r,c = q.popleft()
    if r < 0 or r >= R2 or c < 0 or c >= C2:
        continue
    
    if grid2[r][c] == "1":
        grid2[r][c] = "0"
        for dr,dc in dirs:
            q.append((r+dr, c+dc))

# count remaining valid squares
part2 = 0
for r in range(0,R2,2):
    for c in range(0,C2,2):
        if grid2[r][c] == "1":
            part2 += 1

print(part1, part2)
