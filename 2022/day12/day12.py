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

S = None
E = None
possible = []

for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == 'S':
            S = (i, j)
            map[i][j] = 'a'
        elif map[i][j] == 'E':
            E = (i, j)
            map[i][j] = 'z'
        if map[i][j] == 'a':
            possible.append((i, j))


def get_dist(start):
    curr = {}
    queue = deque()
    queue.append((start, 0))
    while queue:
        (x, y), dist = queue.pop()

        if (x, y) not in curr or dist < curr[(x, y)]:
            curr[(x, y)] = dist
            for r, c in d:
                if 0 <= x+r < len(map) and 0 <= y+c < len(map[0]) and ord(map[x+r][y+c]) - ord(map[x][y]) <= 1:
                    queue.appendleft(((x+r, y+c), dist + 1))
    return curr.get(E, None)


part1 = get_dist(S)
part2 = min([d for d in [get_dist((x, y)) for x, y in possible] if d])
print(part1)
print(part2)
