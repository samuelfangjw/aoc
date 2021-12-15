import sys
import heapq

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
grid = []

with open(file) as f:
    for line in f:
        line = [int(x) for x in line.strip()]
        grid.append(line)

def get_neighbours(x,y):
    nbs = []
    for x1,y1 in [(x-1,y), (x, y-1), (x,y+1), (x+1, y)]:
        if 0 <= x1 < rows and 0 <= y1 < cols and (x1,y1) not in visited:
            nbs.append((x1, y1))
    return nbs

def solve():
    global rows, cols, visited
    pq = []
    visited = set()
    rows = len(grid)
    cols = len(grid[0])
    end = (rows-1, cols-1)
    while pq:
        c, (x,y) = heapq.heappop(pq)
        if (x,y) in visited:
            continue
        if (x,y) == end:
            print(c)
            break
        visited.add((x,y))
        nbs = get_neighbours(x,y)
        for x1,y1 in nbs:
            heapq.heappush(pq, (c + grid[x1][y1], (x1,y1)))

solve()

f = lambda i, j: (grid[j % len(grid[0])][i % len(grid)] + i // len(grid) + j // len(grid[0]) - 1) % 9 + 1
grid = [[f(i,j) for i in range(len(grid[0]) * 5)] for j in range(len(grid) * 5)]

solve()
