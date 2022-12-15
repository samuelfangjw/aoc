import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = f.read()

y = 2000000
mxy = 4000000


def dist(sx, sy, bx, by):
    return abs(sx-bx) + abs(sy-by)


sensors = []
nobeacon1 = set()
beacon1 = set()

for line in data.splitlines():
    tokens = line.replace('x=', '').replace(
        'y=', '').replace(',', '').replace(':', '').split()
    sx = int(tokens[2])
    sy = int(tokens[3])
    bx = int(tokens[8])
    by = int(tokens[9])
    d = dist(sx, sy, bx, by)
    sensors.append((sx, sy, bx, by, d))

for sx, sy, bx, by, d in sensors:
    if by == y:
        beacon1.add(bx)
    if d >= abs(sy - y):
        # abs(sx-x) + abs(sy-y) = d
        # sx + x = d - abs(sy-y) OR sx + x = -d + abs(sy-y)
        x1 = d - abs(sy - y) + sx
        x2 = -d + abs(sy - y) + sx
        x1, x2 = min(x1, x2), max(x1, x2)
        nobeacon1.update([i for i in range(x1, x2+1)])
        # assert dist(sx, sy, x1, y) == d
        # assert dist(sx, sy, x2, y) == d

nobeacon1.difference_update(beacon1)
part1 = len(nobeacon1)
print(part1)

for y in range(mxy):
    ranges = []
    for sx, sy, bx, by, d in sensors:
        if d >= abs(sy - y):
            # abs(sx-x) + abs(sy-y) = d
            # sx + x = d - abs(sy-y) OR sx + x = -d + abs(sy-y)
            x1 = d - abs(sy - y) + sx
            x2 = -d + abs(sy - y) + sx
            x1, x2 = min(x1, x2), max(x1, x2)
            if x1 <= mxy and x2 >= 0:
                ranges.append((x1, x2))
    ranges = sorted(ranges)
    mx = 0
    for x1, x2 in ranges:
        if x1 > mx:
            break
        mx = max(mx, x2)

    if mx < mxy:
        part2 = (mx + 1) * mxy + y
        break

print(part2)
