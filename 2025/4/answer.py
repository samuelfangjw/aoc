import sys

grid = []

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    grid = [list(line) for line in f.read().strip().split("\n")]

dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
n, m = len(grid), len(grid[0])

cycles = []

while True:
    removed = set()

    for i in range(n):
        for j in range(m):
            if grid[i][j] != "@":
                continue

            rolls = sum(
                1
                for di, dj in dirs
                if 0 <= i + di < n and 0 <= j + dj < m and grid[i + di][j + dj] == "@"
            )

            if rolls < 4:
                removed.add((i, j))

    if not removed:
        break

    cycles.append(len(removed))
    for i, j in removed:
        grid[i][j] = "."


print("Part 1:", cycles[0])
print("Part 2:", sum(cycles))
