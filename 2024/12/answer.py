import sys
from collections import deque

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    grid = []
    for line in f:
        line = line.strip()
        grid.append(line)

checked = set()
part1, part2 = 0, 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if (i,j) in checked:
            continue

        queue = deque([(i,j)])
        same_plot = set()

        while queue:
            x, y = queue.popleft()

            if (x,y) in same_plot:
                continue

            same_plot.add((x,y))
            
            for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                if 0 <= x+dx < len(grid) and 0 <= y+dy < len(grid[x+dx]) and grid[x+dx][y+dy] == grid[i][j]:
                    queue.append((x+dx,y+dy))
        
        checked.update(same_plot)

        area = len(same_plot)
        perimeter_one = 0
        perimeter_segments = set()

        for x, y in same_plot:
            for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                if (x+dx,y+dy) not in same_plot:
                    perimeter_one += 1
                    if (dx, dy) == (0,1):
                        perimeter_segments.add((x,y+1,"b"))
                    elif (dx, dy) == (1,0):
                        perimeter_segments.add((x+1,y,"r"))
                    elif (dx, dy) == (0,-1):
                        perimeter_segments.add((x,y,"t"))
                    else:
                        perimeter_segments.add((x,y,"l"))

        part1 += area * perimeter_one

        for x, y, d in list(perimeter_segments):
            if (x, y, d) not in perimeter_segments:
                continue
            dx, dy = 1 if d in ["b", "t"] else 0, 1 if d in ["r", "l"] else 0

            nx, ny = x+dx, y+dy
            while (nx, ny, d) in perimeter_segments:
                perimeter_segments.remove((nx, ny, d))
                nx, ny = nx+dx, ny+dy
            nx, ny = x-dx, y-dy
            while (nx, ny, d) in perimeter_segments:
                perimeter_segments.remove((nx, ny, d))
                nx, ny = nx-dx, ny-dy

        part2 += area * len(perimeter_segments)

print("Part 1:", part1)
print("Part 2:", part2)
