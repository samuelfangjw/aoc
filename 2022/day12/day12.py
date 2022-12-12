import sys
from collections import deque

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = []

with open(file) as f:
    for line in f:
        data.append(line.strip())

map = []
for line in data:
    map.append(list(line))

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == 'S':
            S = (i, j)
            map[i][j] = 'a'
        elif map[i][j] == 'E':
            E = (i, j)
            map[i][j] = 'z'

seen = set()
queue = deque()
queue.append((E, 0))

part2 = 10000
while queue:
    (x, y), dist = queue.pop()

    if (x, y) in seen:
        continue
    seen.add((x, y))

    if map[x][y] == 'a':
        part2 = min(dist, part2)
    if (x, y) == S:
        part1 = dist

    for r, c in d:
        if 0 <= x+r < len(map) and 0 <= y+c < len(map[0]) and ord(map[x][y]) - ord(map[x+r][y+c]) <= 1:
            queue.appendleft(((x+r, y+c), dist + 1))

print(part1)
print(part2)
