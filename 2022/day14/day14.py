import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = f.read()

start = (500, 0)
maxY = 0
grid = set()

for line in data.strip().split('\n'):
    points = [list(map(int, point.split(','))) for point in line.split(' -> ')]
    for (x1, y1), (x2, y2) in zip(points[:-1], points[1:]):
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid.add((x1, y))
        else:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid.add((x, y1))
        maxY = max(maxY, y1)
        maxY = max(maxY, y2)

part1 = 0
found = False
part2 = 0

while True:
    x, y = start

    for _ in range(maxY + 1):
        if (x, y + 1) not in grid:
            y += 1
        elif (x - 1, y + 1) not in grid:
            x -= 1
            y += 1
        elif (x + 1, y + 1) not in grid:
            x += 1
            y += 1
        else:
            break

    grid.add((x, y))

    part2 += 1
    if x == 500 and y == 0:
        break
    elif y >= maxY:
        found = True

    if not found:
        part1 += 1

print(part1)
print(part2)
