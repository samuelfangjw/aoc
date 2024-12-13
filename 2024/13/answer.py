import sys
import re

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = []
    pattern = re.compile(r'X[\+=](\d+), Y[\+=](\d+)')
    for section in f.read().split('\n\n'):
        lines = section.splitlines()
        a = re.findall(pattern, lines[0])
        b = re.findall(pattern, lines[1])
        c = re.findall(pattern, lines[2])
        data.append([int(x) for x in (a[0][0], a[0][1], b[0][0], b[0][1], c[0][0], c[0][1])])

def solve(ax, ay, bx, by, px, py):
    j = (py * ax - px * ay) / (by * ax - bx * ay)
    i = (px * by - bx * py)  / (ax * by - ay * bx)
    return [i, j]

part1, part2 = 0, 0
for ax, ay, bx, by, px, py in data:
    i, j = solve(ax, ay, bx, by, px, py)
    if i.is_integer() and j.is_integer() and i >= 0 and j >= 0:
        part1 += int(3 * i + j)

    px += 10000000000000
    py += 10000000000000

    i, j = solve(ax, ay, bx, by, px, py)

    if i.is_integer() and j.is_integer() and i >= 0 and j >= 0:
        part2 += int(3 * i + j)

print("Part 1:", part1)
print("Part 2:", part2)
