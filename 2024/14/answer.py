import sys
import re

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    pattern = re.compile(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)')
    data = re.findall(pattern, f.read())
    data = [(int(a), int(b), int(c), int(d)) for a, b, c, d in data]


C, R = 101, 103

qtl, qtr, qbl, qbr = 0, 0 ,0, 0

def get_next_pos(px, py, vx, vy):
    px += vx
    py += vy
    px = px % C
    py = py % R

    return [px, py]

for px, py, vx, vy in data:
    x, y = px, py
    for _ in range(100):
        x, y = get_next_pos(x, y, vx, vy)

    if 0 <= y < R // 2 and 0 <= x < C // 2:
        qtl += 1
    elif R // 2 < y < R and 0 <= x < C // 2:
        qbl += 1
    elif 0 <= y < R // 2 and C // 2 < x < C:
        qtr += 1
    elif R // 2 < y < R and C // 2 < x < C:
        qbr += 1

part1 = qtl * qtr * qbl * qbr

print("Part 1:", part1)

grid = [['.' for _ in range(C)] for _ in range(R)]

for px, py, vx, vy in data:
    grid[py][px] = "#"

for i in range(7000):
    for idx, (px, py, vx, vy) in enumerate(data):
        grid[py][px] = '.'
        px, py = get_next_pos(px, py, vx, vy)
        grid[py][px] = '#'
        data[idx] = (px, py, vx, vy)
    
    print("Iteration: ", i+1)
    for row in grid:
        print(''.join(row))

# for part 2, pipe output to txt file and manually search for the christmas tree. The answer was 6644 in my input.
