import sys
import re

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    grid, path = f.read().split('\n\n')

grid = grid.splitlines()
path = re.findall('\d+|L|R', path)


d = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]

mapping = {}

for i in range(50):
    mapping[((0, 50+i), 3)] = ((150+i, 0), 0)
    mapping[((150+i, 0), 2)] = ((0, 50+i), 1)

    mapping[((150-1, 50+i), 1)] = ((150+i, 50-1), 2)
    mapping[((150+i, 50-1), 0)] = ((150-1, 50+i), 3)

    mapping[((0, 100+i), 3)] = ((200-1, 0+i), 3)
    mapping[((200-1, 0+i), 1)] = ((0, 100+i), 1)

    mapping[((50-1, 100+i), 1)] = ((50+i, 100-1), 2)
    mapping[((50+i, 100-1), 0)] = ((50-1, 100+i), 3)

    mapping[((0+i, 150-1), 0)] = ((150-1-i, 100-1), 2)
    mapping[((100+i, 100-1), 0)] = ((50-1-i, 150-1), 2)

    mapping[((50+i, 50), 2)] = ((100, 0+i), 1)
    mapping[((100, 0+i), 3)] = ((50+i, 50), 0)

    mapping[((0+i, 50), 2)] = ((150-1-i, 0), 0)
    mapping[((100+i, 0), 2)] = ((50-1-i, 50), 0)

# FOR EXAMPLE
# for i in range(4):
#     mapping[((4+i, 12-1), 0)] = ((8, 12+i), 1)
#     mapping[((8, 12+i), 3)] = ((4+i, 12-1), 2)

#     mapping[((0+i, 12-1), 0)] = ((8+i, 16-1), 2)
#     mapping[((8+i, 16-1), 2)] = ((0+i, 12-1), 0)

#     mapping[((0+i, 8), 2)] = ((4, 4+i), 1)
#     mapping[((4, 4+i), 3)] = ((0+i, 8), 0)

#     mapping[((8+i, 8), 2)] = ((8-1, 4+i), 3)
#     mapping[((8-1, 4+i), 1)] = ((8+i, 8), 0)

#     mapping[((4+i, 0), 2)] = ((12-1, 12+i), 3)
#     mapping[((12-1, 12+i), 1)] = ((4+i, 0), 0)

#     mapping[((4, 0+i), 3)] = ((0, 8+i), 1)
#     mapping[((0, 8+i), 3)] = ((4, 0+i), 1)

#     mapping[((8-1, 0+i), 1)] = ((12-1, 8+i), 3)
#     mapping[((12-1, 8+i), 1)] = ((8-1, 0+i), 3)


def solve(part):
    facing = 0  # right, down, left, up
    pos = (0, 0)  # r, c

    while grid[pos[0]][pos[1]] == ' ':
        pos = (pos[0], pos[1] + 1)

    for inst in path:
        if inst == 'L':
            facing = (facing - 1) % 4
        elif inst == 'R':
            facing = (facing + 1) % 4
        else:
            x = int(inst)
            d1 = d[facing]
            for _ in range(x):
                nxt = (pos[0] + d1[0], pos[1] + d1[1])
                if not 0 <= nxt[0] < len(grid) or not 0 <= nxt[1] < len(grid[nxt[0]]) or grid[nxt[0]][nxt[1]] == ' ':
                    # Handle wrap-around
                    if part == 1:
                        d2 = (-d1[0], -d1[1])
                        nxt = pos
                        tmp = (pos[0] + d2[0], pos[1] + d2[1])
                        while 0 <= tmp[0] < len(grid) and 0 <= tmp[1] < len(grid[tmp[0]]) and grid[tmp[0]][tmp[1]] != ' ':
                            nxt = tmp
                            tmp = (tmp[0] + d2[0], tmp[1] + d2[1])
                    elif part == 2:
                        nxt, newfacing = mapping[(pos, facing)]
                        if grid[nxt[0]][nxt[1]] == '#':
                            break
                        facing = newfacing
                        d1 = d[newfacing]
                if grid[nxt[0]][nxt[1]] == '#':
                    break
                pos = nxt
    return (pos[0] + 1) * 1000 + (pos[1] + 1) * 4 + facing


part1 = solve(1)
print(part1)

part2 = solve(2)
print(part2)
