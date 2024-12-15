import sys
from copy import deepcopy

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    grid0, actions = f.read().strip().split("\n\n")
    grid0 = [list(row) for row in grid0.split("\n")]
    actions = actions.replace("\n", "")

dirs = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}

for i, j in [(i, j) for i in range(len(grid0)) for j in range(len(grid0[0]))]:
        if grid0[i][j] == "@":
            pos = (i, j)
            grid0[i][j] = "."
            break

def solve1(pos):
    gps_coordinates = 0
    grid = deepcopy(grid0)
    R, C = len(grid), len(grid[0])


    for action in actions:
        dx, dy = dirs[action]
        nx, ny = pos[0] + dx, pos[1] + dy

        if grid[nx][ny] == ".":
            pos = (nx, ny)
            continue
        elif grid[nx][ny] == "#":
            continue
        
        while grid[nx][ny] == "O":
            nx, ny = nx + dx, ny + dy

        if grid[nx][ny] == "#":
            continue
        else:
            grid[nx][ny] = "O"
            nx, ny = pos[0] + dx, pos[1] + dy
            grid[nx][ny] = "."
            pos = (nx, ny)

    for i, j in [(i, j) for i in range(R) for j in range(C)]:
        if grid[i][j] == "O":
            gps_coordinates += i * 100 + j
    
    return gps_coordinates

def solve2(pos):
    gps_coordinates = 0
    grid = [["." for _ in range(len(grid0[0]) * 2)] for _ in range(len(grid0))]

    for i, j in [(i, j) for i in range(len(grid0)) for j in range(len(grid0[0]))]:
        if grid0[i][j] == ".":
            continue
        elif grid0[i][j] == "#":
            grid[i][j*2] = "#"
            grid[i][j*2+1] = "#"
        elif grid0[i][j] == "O":
            grid[i][j*2] = "["
            grid[i][j*2+1] = "]"

    R, C = len(grid), len(grid[0])
    
    def move_boxes(x, y, dx, dy, execute):
        if grid[x][y] == "#":
            return "#"
        elif grid[x][y] == ".":
            return "."
        
        if dy and move_boxes(x, y + dy, dx, dy, execute) == ".":
            if execute:
                grid[x][y + dy] = grid[x][y]
                grid[x][y] = "."
            return "."
        elif dx:
            if grid[x][y] == "[":
                left = move_boxes(x + dx, y, dx, dy, execute) == "."
                right = move_boxes(x + dx, y + 1, dx, dy, execute) == "."
                if left and right:
                    if execute:
                        grid[x + dx][y] = grid[x][y]
                        grid[x + dx][y + 1] = grid[x][y + 1]
                        grid[x][y] = "."
                        grid[x][y + 1] = "."
                    return "."
            else:
                left = move_boxes(x + dx, y - 1, dx, dy, execute) == "."
                right = move_boxes(x + dx, y, dx, dy, execute) == "."
                if left and right:
                    if execute:
                        grid[x + dx][y - 1] = grid[x][y - 1]
                        grid[x + dx][y] = grid[x][y]
                        grid[x][y - 1] = "."
                        grid[x][y] = "."
                    return "."
        return "#" 

    for action in actions:
        dx, dy = dirs[action]
        nx, ny = pos[0] + dx, pos[1] + dy

        if grid[nx][ny] == ".":
            pos = (nx, ny)
            continue
        elif grid[nx][ny] == "#":
            continue
        
        if move_boxes(nx, ny, dx, dy, False) == ".":
            move_boxes(nx, ny, dx, dy, True)
            pos = (nx, ny)

    for i, j in [(i, j) for i in range(R) for j in range(C)]:
        if grid[i][j] == "[":
            gps_coordinates += i * 100 + j

    return gps_coordinates

print("Part 1:", solve1(pos))
print("Part 2:", solve2((pos[0], pos[1] * 2)))
