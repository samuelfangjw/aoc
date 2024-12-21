import sys
from collections import deque

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    b = []
    for line in f:
        line = line.strip().split(",")
        b.append([int(x) for x in line])

grid = [[0 for _ in range(71)] for _ in range(71)]

for i in range(1024):
    x, y = b[i]
    grid[x][y] = 1

start = (0, 0)
goal = (70, 70)

def bfs():
    queue = deque([(start, 0)])
    seen = set([start])
    while queue:
        (r, c), s = queue.popleft()
        if (r, c) == goal:
            return s
        for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            if 0 <= nr < 71 and 0 <= nc < 71 and (nr, nc) not in seen and grid[nr][nc] != 1:
                queue.append(((nr, nc), s+1))
                seen.add((nr, nc))
    return -1

print('Part 1:', bfs())

for i in range(1024, len(b)):
    x, y = b[i]
    grid[x][y] = 1
    if bfs() == -1:
        print('Part 2:', str(b[i][0]) + "," + str(b[i][1]))
        break
