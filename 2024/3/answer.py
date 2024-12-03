import sys
import re

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = []
    for line in f:
        line = line.strip()
        pattern = re.compile(r'mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))')
        res = re.findall(pattern, line)
        data.extend(res)

part1, part2 = 0, 0
is_valid = True

for x, y, do, dont in data:
    if do:
        is_valid = True
    elif dont:
        is_valid = False
    else:
        part1 += int(x) * int(y)
        part2 += int(x) * int(y) * int(is_valid)

print("Part 1:", part1)
print("Part 2:", part2)
