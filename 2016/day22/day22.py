import sys
import itertools
import re
from collections import deque

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    grid = {}
    for line in f:
        if line.startswith("/dev"):
            line = line.strip()
            # x, y, size, used, avail%
            pattern = r'/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s'
            res = re.search(pattern, line)
            data = [int(x) for x in res.groups()]
            grid[(data[0], data[1])] = data[2:]

start_node = (0, 0)
goal_node = (max([n[0] for n in grid if n[1] == 0]), 0)
empty_node = next(n for n in grid if grid[n][1] == 0)

part1 = 0
for n1, n2 in itertools.combinations(grid.keys(), 2):
    x1, y1 = n1
    size1, used1, avail1 = grid[n1]
    x2, y2 = n2
    size2, used2, avail2 = grid[n2]

    if used1 > 0 and used1 <= avail2:
        part1 += 1
    
    if used2 > 0 and used2 <= avail1:
        part1 += 1


part2 = 0

def bfs(start, end):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        node, steps = queue.popleft()
        if node == end:
            return steps
        if node in visited:
            continue
        visited.add(node)

        x, y = node
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_node = (x + dx, y + dy)
            if new_node in grid and grid[new_node][1] <= grid[empty_node][0] and new_node != goal_node:
                queue.append((new_node, steps[:] + [new_node]))
    


ideal_path = bfs(goal_node, start_node)
for node in ideal_path:
    path = bfs(empty_node, node)
    part2 += len(path)
    empty_node, goal_node = goal_node, node

part2 += len(ideal_path)

print("Part 1:", part1)
print("Part 2:", part2)
