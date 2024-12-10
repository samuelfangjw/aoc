import sys
from collections import deque

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    grid = []
    for line in f:
        line = line.strip()
        grid.append([int(x) for x in line])

R, C = len(grid), len(grid[0])
trailheads = []

for r in range(R):
    for c in range(C):
        if grid[r][c] == 0:
            trailheads.append((r, c))

part1, part2 = 0, 0

def bfs(start_r, start_c):
    global part1, part2
    queue = deque([(start_r, start_c)])
    visited = set()
    count = 0

    while queue:
        r, c = queue.popleft()

        if grid[r][c] == 9:
            if (r, c) not in visited:
                part1 += 1
                visited.add((r, c))
            part2 += 1
            continue

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < R and 0 <= new_c < C and grid[new_r][new_c] - grid[r][c] == 1:
                queue.append((new_r, new_c))

    return count

for (r, c) in trailheads:
    bfs(r, c)

print("Part 1:", part1)
print("Part 2:", part2)
