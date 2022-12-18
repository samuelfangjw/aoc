import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = f.read().strip()

cubes = set()
for line in data.splitlines():
    x, y, z = map(int, line.split(','))
    cubes.add((x, y, z))

d = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
airpockets = []
minx, maxx, miny, maxy, minz, maxz = 100, -100, 100, -100, 100, -100
for x, y, z in cubes:
    minx, miny, minz = min(minx, x), min(miny, y), min(minz, z)
    maxx, maxy, maxz = max(maxx, x), max(maxy, y), max(maxz, z)
    sides = [(x1, y1, z1) for x1, y1, z1 in [(x+dx, y+dy, z+dz)
                                             for dx, dy, dz in d] if (x1, y1, z1) not in cubes]
    airpockets.extend(sides)

part1 = len(airpockets)
print(part1)

part2 = part1
memo = set()  # keep track of internal air pockets
for x, y, z in airpockets:
    visited = set()
    stack = [(x, y, z)]
    # skip processing if air pocket has already been checked
    found = (x, y, z) in memo

    while stack and not found:
        x1, y1, z1 = stack.pop()
        if (x1, y1, z1) in visited or (x1, y1, z1) in cubes:
            continue

        visited.add((x1, y1, z1))

        if x1 < minx or x1 > maxx or y1 < miny or y1 > maxy or z1 < minz or z1 > maxz:
            found = True
            break

        stack.extend([(x1+dx, y1+dy, z1+dz) for dx, dy, dz in d])

    if not found or (x, y, z) in memo:
        part2 -= 1
        memo.update(visited)

print(part2)
