import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
grid = []

with open(file) as f:
    for line in f:
        line = line.strip()
        grid.append(list(line))

# Part 1
part1 = 0
for c in range(len(grid[0])):
    i = 0
    for r in range(len(grid)):
        if grid[r][c] == '#':
            i = r + 1
        elif grid[r][c] == 'O':
            part1 += len(grid) - i
            i += 1

# Part 2
part2 = 0
i, n = 0, 1000000000 * 4
prev = []
found = False
while i < n:
    if i % 4 == 0:
        # North
        for c in range(len(grid[0])):
            j = 0
            for r in range(len(grid)):
                if grid[r][c] == '#':
                    j = r + 1
                elif grid[r][c] == 'O':
                    grid[r][c] = '.'
                    grid[j][c] = 'O'
                    j += 1
    elif i % 4 == 1:
        # West
        for r in range(len(grid)):
            j = 0
            for c in range(len(grid[0])):
                if grid[r][c] == '#':
                    j = c + 1
                elif grid[r][c] == 'O':
                    grid[r][c] = '.'
                    grid[r][j] = 'O'
                    j += 1
    elif i % 4 == 2:
        # South
        for c in range(len(grid[0])):
            j = len(grid)-1
            for r in range(len(grid)-1, -1, -1):
                if grid[r][c] == '#':
                    j = r - 1
                elif grid[r][c] == 'O':
                    grid[r][c] = '.'
                    grid[j][c] = 'O'
                    j -= 1
    else:
        # East
        for r in range(len(grid)):
            j = len(grid[0])-1
            for c in range(len(grid[0])-1, -1, -1):
                if grid[r][c] == '#':
                    j = c - 1
                elif grid[r][c] == 'O':
                    grid[r][c] = '.'
                    grid[r][j] = 'O'
                    j -= 1
    
    if not found:
        for k, g in prev:
            if grid == g:
                found = True
                x = i - k
                left = n - i
                i = n - (left % x)
        prev.append((i, [[x for x in y] for y in grid]))
    i += 1

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 'O':
            part2 += len(grid) - r

print(part1, part2)
