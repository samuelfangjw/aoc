import sys
from collections import defaultdict

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = defaultdict(list)

with open(file) as f:
    for line in f:
        a,b = line.strip().split("-")
        if b != 'start':
            data[a].append(b)
        if a != 'start':
            data[b].append(a)

def bfs(x, visited):
    global part1, part2
    if x == 'end':
        if not visited[0]:
            part1 += 1
        part2 += 1
        return
    for y in data[x]:
        if x.isupper():
            bfs(y, visited)
        elif x not in visited:
            bfs(y, visited + [x])
        elif not visited[0]:
            bfs(y, [True] + visited[1:])

part1 = 0
part2 = 0

bfs('start', [False])

print(part1)
print(part2)
