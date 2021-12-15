import sys
import heapq
from collections import defaultdict
import math

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
grid = []

with open(file) as f:
    for line in f:
        line = [int(x) for x in line.strip()]
        grid.append(line)

def get_neighbours(x,y):
    nbs = []
    for x1,y1 in [(x-1,y), (x, y-1), (x,y+1), (x+1, y)]:
        if 0 <= x1 < rows and 0 <= y1 < cols and (x1,y1):
            nbs.append((x1, y1))
    return nbs

def manhatten(i,j,x,y):
    return abs(i-x) + abs(j-y)

def solve():
    global rows, cols, visited
    pq = []
    costs = defaultdict(lambda:math.inf)
    visited = set()
    rows = len(grid)
    cols = len(grid[0])
    end = (rows-1, cols-1)
    heapq.heappush(pq, (0 + manhatten(0,0,rows-1,cols-1), (0,0)))
    costs[(0,0)] = 0
    while pq:
        _, (x,y) = heapq.heappop(pq)
        if (x,y) in visited:
            continue
        if (x,y) == end:
            print(costs[(x,y)])
            break
        visited.add((x,y))
        nbs = get_neighbours(x,y)
        c = costs[(x,y)]
        for x1,y1 in nbs:
            c1 = c + grid[x1][y1]
            if c1 < costs[(x1,y1)]:
                costs[(x1,y1)] = c1
                heapq.heappush(pq, (costs[(x1,y1)] + manhatten(y1,x1,end[0],end[1]), (x1,y1)))

solve()

f = lambda i, j: (grid[j % len(grid[0])][i % len(grid)] + i // len(grid) + j // len(grid[0]) - 1) % 9 + 1
grid = [[f(i,j) for i in range(len(grid[0]) * 5)] for j in range(len(grid) * 5)]

solve()
