import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    input = [x.strip().split(" -> ") for x in f.readlines()]
    input = [x.split(",") + y.split(",") for x, y in input]
    input = [[int(x) for x in line] for line in input]

size = 1000
grid = [[0 for _ in range(size)] for _ in range(size)]

# Part 1
for x1, y1, x2, y2 in input:
    if x1 == x2:
        for i in range(min(y1,y2), max(y2, y1) + 1):
            grid[x1][i] += 1
    elif y1 == y2:
        for i in range(min(x1,x2), max(x1,x2) + 1):
            grid[i][y1] += 1

part1 = sum([sum([1 for num in row if num > 1]) for row in grid])

# Part 2
for x1, y1, x2, y2 in input:
    if x1 != x2 and y1 != y2:
        if x1 > x2:
            x1, x2, y1, y2 = x2, x1, y2, y1

        if y2 > y1:
            for i in range(x1, x2 + 1):
                grid[i][y1] += 1
                y1 += 1
        else:
            for i in range(x1, x2 + 1):
                grid[i][y1] += 1
                y1 -= 1

part2 = sum([sum([1 for num in row if num > 1]) for row in grid])

print(part1)
print(part2)