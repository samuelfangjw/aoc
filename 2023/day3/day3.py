import sys
from collections import defaultdict

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
grid = []

with open(file) as f:
    for line in f:
        line = line.strip()
        grid.append(list(line))

R, C = len(grid), len(grid[0])

# (num, row, start, end)
nums = []

for r, row in enumerate(grid):
    start = 0
    num = ""
    for c, char in enumerate(row):
        if char.isdigit():
            num += char
        elif num:
            nums.append((int(num), r, start, c - 1))
            num = ""
            start = c + 1
        else:
            start += 1
    if num:
        nums.append((int(num), r, start, c - 1))

part1, part2 = 0, 0
gears = defaultdict(list)

for num, row, start, end in nums:
    possible = False
    to_check = [
        (row, start-1),
        (row, end + 1)
    ]
    to_check.extend([(row-1, x) for x in range(start-1, end + 2)])
    to_check.extend([(row+1, x) for x in range(start-1, end + 2)])

    for x, y in to_check:
        if x < 0 or x >= R or y < 0 or y >= C:
            continue
        if not grid[x][y].isdigit() and not grid[x][y] == '.':
            possible = True
        if grid[x][y] == '*':
            gears[(x, y)].append(num)

    if possible:
        part1 += num

for x, y in [x for x in gears.values() if len(x) == 2]:
    part2 += x * y

print(part1, part2)
