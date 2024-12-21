from functools import cache
import sys
from collections import defaultdict

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    towels = f.readline().strip().split(", ")
    f.readline()
    designs = []
    for line in f.readlines():
        line = line.strip()
        designs.append(line)

startswith = defaultdict(list)

for towel in towels:
    startswith[towel[0]].append(towel)

@cache
def recurse(design):
    if design == "":
        return 1
    
    count = 0
    for towel in startswith[design[0]]:
        if design.startswith(towel):
            r = recurse(design[len(towel):])
            count += r

    return count

part1, part2 = 0, 0
for design in designs:
    c = recurse(design)
    if c:
        part1 += 1
    part2 += c
    
print("Part 1:", part1)
print("Part 2:", part2)
