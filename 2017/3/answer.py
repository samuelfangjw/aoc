import sys
from collections import defaultdict

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = int(f.read().strip())

x, y = 0,0
limit = 1
count = 1
direction = "R"

grid = defaultdict(int)
grid[(0, 0)] = 1

found = False

def manhattan_distance(x, y):
    return abs(x) + abs(y)

while True:
    count += 1

    if direction == "R":
        x = x + 1
        if x == limit:
            direction = "U"
    elif direction == "U":
        y = y + 1
        if y == limit:
            direction = "L"
    elif direction == "L":
        x = x - 1
        if x == -limit:
            direction = "D"
    elif direction == "D":
        y = y - 1
        if y == -limit:
            direction = "R"
            limit = limit + 1

    grid[(x, y)] = sum([grid[(x + i, y + j)] for i in range(-1, 2) for j in range(-1, 2)])
    
    if grid[(x, y)] > data and not found:
        part2 = grid[(x, y)]
        found = True

    if count == data:
        part1 = manhattan_distance(x, y)
        break

print("Part 1:", part1)
print("Part 2:", part2)
