import sys
import itertools

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = []
    for line in f:
        line = line.strip().split()
        data.append([int(x) for x in line])

part1, part2 = 0, 0
for row in data:
    part1 += max(row) - min(row)
    for x, y in itertools.combinations(row, 2):
        if x % y == 0:
            part2 += x // y
            break
        elif y % x == 0:
            part2 += y // x
            break

print("Part 1:", part1)
print("Part 2:", part2)
