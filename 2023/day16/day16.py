import sys
from collections import defaultdict, deque

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
grid = []

with open(file) as f:
    for line in f:
        line = line.strip()
        grid.append(line)

dirs = {
    'N': (-1,0),
    'S': (1,0),
    'E': (0,1),
    'W': (0,-1)
}

mirrors = {
    '|': {
        'E': ['N', 'S'],
        'W': ['N', 'S'],
        'N': ['N'],
        'S': ['S']
    },
    '-': {
        'N': ['W', 'E'],
        'S': ['W', 'E'],
        'E': ['E'],
        'W': ['W']
    },
    '\\': {
        'E': ['S'],
        'W': ['N'],
        'N': ['W'],
        'S': ['E']
    },
    '/': {
        'E': ['N'],
        'W': ['S'],
        'N': ['E'],
        'S': ['W']
    },
    '.': {
        'E': ['E'],
        'W': ['W'],
        'N': ['N'],
        'S': ['S']
    }
}

def solve(ro,co,do):
    q = deque()
    q.append((ro,co,do))
    seen = defaultdict(list)

    while q:
        r,c,d = q.popleft()
        if d in seen[(r,c)]:
            continue
        seen[(r,c)].append(d)

        ndirs = mirrors[grid[r][c]][d]
        for ndir in ndirs:
            dr, dc = dirs[ndir]
            nr, nc = r+dr, c+dc
            if 0<=nr<len(grid) and 0<=nc<len(grid[0]):
                q.append((nr,nc,ndir))
    return len(seen)

part1, part2 = solve(0,0,'E'), 0

for i in range(len(grid)):
    part2 = max(part2, solve(i,0,'E'), solve(i,len(grid[0])-1,'W'))

for i in range(len(grid[0])):
    part2 = max(part2, solve(0,i,'S'), solve(len(grid)-1,i,'N'))

print(part1, part2)
