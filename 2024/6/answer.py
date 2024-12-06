import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    grid = []
    for line in f:
        line = line.strip()
        grid.append(list(line))

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '^':
            start = (i, j)

def is_wall(x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '#'

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# part 1
x,y = start
facing = 0
visited = set()

while 0 <= x < len(grid) and 0 <= y < len(grid[0]):
    visited.add((x, y))
    dx, dy = d[facing]
    nx, ny = x+dx, y+dy

    while is_wall(nx, ny):
        facing = (facing + 1) % 4
        dx, dy = d[facing]
        nx, ny = x+dx, y+dy
    
    x, y = nx, ny
    
# part 2
part2 = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != '.':
            continue
        
        grid[i][j] = '#'
        x,y = start
        facing = 0

        visited = set()

        while 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            if (x, y, facing) in visited:
                part2 += 1
                break
            visited.add((x, y, facing))
            dx, dy = d[facing]
            nx, ny = x+dx, y+dy

            while is_wall(nx, ny):
                facing = (facing + 1) % 4
                dx, dy = d[facing]
                nx, ny = x+dx, y+dy
            
            x, y = nx, ny
        
        grid[i][j] = '.'

print("Part 1:", len(visited))
print("Part 2:", part2)
