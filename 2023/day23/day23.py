import sys
from collections import defaultdict

sys.setrecursionlimit(10000)

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
grid = []

with open(file) as f:
    for line in f:
        line = line.strip()
        grid.append(list(line))

start, end = (0,1), (len(grid)-1, len(grid[0])-2)

def dfs1(node, visited):
    if node == end:
        return 0

    r,c = node
    ans = 0

    for dr,dc in [(0,1), (0,-1), (1,0), (-1,0)]:
        r2,c2 = r+dr,c+dc
        if 0<=r2<len(grid) and 0<=c2<len(grid[0]) and (r2,c2) not in visited:
            visited.add((r2,c2))
            if grid[r2][c2] == '.':
                ans = max(dfs1((r2,c2), visited) + 1, ans)
            elif grid[r2][c2] == '>' and dc == 1 or grid[r2][c2] == '<' and dc == -1:
                ans = max(dfs1((r2,c2), visited) + 1, ans)
            elif grid[r2][c2] == '^' and dr == -1 or grid[r2][c2] == 'v' and dr == 1:
                ans = max(dfs1((r2,c2), visited) + 1, ans)
            visited.remove((r2,c2))

    if ans == 0:
        # invalid path does not lead to end node
        return -10000

    return ans

def dfs2(node, visited):
    if node == end:
        return 0

    r,c = node
    ans = 0

    for r2,c2,l in graph[(r,c)]:
        if (r2,c2) not in visited:
            visited.add((r2,c2))
            ans = max(dfs2((r2,c2), visited) + l, ans)
            visited.remove((r2,c2))

    if ans == 0:
        # invalid path does not lead to end node
        return -10000

    return ans

def neighbors(r,c):
    return [(r+dr,c+dc) for dr,dc in [(0,1), (0,-1), (1,0), (-1,0)] if 0<=r+dr<len(grid) and 0<=c+dc<len(grid[0]) and grid[r+dr][c+dc] != '#']

graph = defaultdict(list)
visited = set()

q = [start]
while q:
    r,c = q.pop()
    if (r,c) in visited:
        continue
    visited.add((r,c))
    
    for r2,c2 in neighbors(r,c):
        prev = (r,c)
        length = 1
        nb = [x for x in neighbors(r2,c2) if x != prev]
        while len(nb) == 1:
            prev = r2,c2
            length += 1
            r2,c2 = nb[0]
            nb = [x for x in neighbors(r2,c2) if x != prev]
        graph[(r,c)].append((r2,c2,length))
        q.append((r2,c2))

part1 = dfs1(start, set([start]))
part2 = dfs2(start, set([start]))

print(part1, part2)
