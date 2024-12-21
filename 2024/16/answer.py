import heapq
import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    grid = []
    for line in f:
        line = line.strip()
        grid.append(line)

R, C = len(grid), len(grid[0])
for i, j in [(i, j) for i in range(R) for j in range(C)]:
    if grid[i][j] == 'S':
        start = (i, j)
    if grid[i][j] == 'E':
        goal = (i, j)

pq = []
heapq.heappush(pq, (0, (start[0], start[1], "E"), set([start])))

seen = {}

best_score = float('inf')
best_tiles = set()

while pq:
    score , (r, c, facing), tiles = heapq.heappop(pq)
    
    if score > best_score:
        break

    if (r, c) == goal:
        best_score = score
        best_tiles.update(tiles)
        continue

    if (r, c, facing) in seen and seen[(r, c, facing)] < score:
        continue
    seen[(r, c, facing)] = score
    
    if facing == "E":
        nr, nc = r, c + 1
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#':
            ntiles = tiles.copy()
            ntiles.add((nr, nc))
            heapq.heappush(pq, (score+1, (nr, nc, "E"), ntiles))
        heapq.heappush(pq, (score+1000, (r, c, "N"), tiles))
        heapq.heappush(pq, (score+1000, (r, c, "S"), tiles))
    elif facing == "W":
        nr, nc = r, c - 1
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#':
            ntiles = tiles.copy()
            ntiles.add((nr, nc))
            heapq.heappush(pq, (score+1, (nr, nc, "W"), ntiles))
        heapq.heappush(pq, (score+1000, (r, c, "N"), tiles))
        heapq.heappush(pq, (score+1000, (r, c, "S"), tiles))
    elif facing == "N":
        nr, nc = r - 1, c
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#':
            ntiles = tiles.copy()
            ntiles.add((nr, nc))
            heapq.heappush(pq, (score+1, (nr, nc, "N"), ntiles))
        heapq.heappush(pq, (score+1000, (r, c, "E"), tiles))
        heapq.heappush(pq, (score+1000, (r, c, "W"), tiles))
    elif facing == "S":
        nr, nc = r + 1, c
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#':
            ntiles = tiles.copy()
            ntiles.add((nr, nc))
            heapq.heappush(pq, (score+1, (nr, nc, "S"), ntiles))
        heapq.heappush(pq, (score+1000, (r, c, "E"), tiles))
        heapq.heappush(pq, (score+1000, (r, c, "W"), tiles))

print("Part 1:", best_score)
print("Part 2:", len(best_tiles))
