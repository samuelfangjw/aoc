import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = []

with open(file) as f:
    for line in f:
        line = line.strip()
        data.append(line)

trees = [list(map(int, d[:])) for d in data]
visible = set()
C = len(trees[0])
R = len(trees)

# left to right
for r in range(R):
    curr = -1
    for c in range(C):
        if trees[r][c] > curr:
            curr = trees[r][c]
            visible.add((r, c))

# right to left
for r in range(R):
    curr = -1
    for c in range(C-1, -1, -1):
        if trees[r][c] > curr:
            curr = trees[r][c]
            visible.add((r, c))

# top to bottom
for c in range(C):
    curr = -1
    for r in range(R):
        if trees[r][c] > curr:
            curr = trees[r][c]
            visible.add((r, c))

# bottom to top
for c in range(C):
    curr = -1
    for r in range(R-1, -1, -1):
        if trees[r][c] > curr:
            curr = trees[r][c]
            visible.add((r, c))

part1 = len(visible)

part2 = 0
for r in range(R):
    for c in range(C):
        down = 0
        curr = trees[r][c]
        for x in range(r+1, R):
            down += 1
            if trees[x][c] >= curr:
                break

        top = 0
        curr = trees[r][c]
        for x in range(r-1, -1, -1):
            top += 1
            if trees[x][c] >= curr:
                break

        right = 0
        curr = trees[r][c]
        for y in range(c+1, C):
            right += 1
            if trees[r][y] >= curr:
                break

        left = 0
        curr = trees[r][c]
        for y in range(c-1, -1, -1):
            left += 1
            if trees[r][y] >= curr:
                break

        part2 = max(part2, left * right * top * down)

print(part1)
print(part2)
