import sys
import bisect

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file, "r") as f:
    grid = [line.strip() for line in f.readlines() if line.strip()]

r, c = len(grid), len(grid[0])

start = (0, grid[0].index("S"))
col_idxs = [[] for _ in range(c)]

for i in range(r):
    for j in range(c):
        if grid[i][j] == "^":
            col_idxs[j].append(i)


first_splitter = (bisect.bisect_right(col_idxs[start[1]], start[0]), start[1])
visited = {}


def dfs(splitter):
    if not splitter:
        return 1

    x, y = splitter
    if (x, y) in visited:
        return visited[(x, y)]

    splitter_left_idx = bisect.bisect_left(col_idxs[y - 1], x)
    splitter_left = (
        (col_idxs[y - 1][splitter_left_idx], y - 1)
        if splitter_left_idx < len(col_idxs[y - 1])
        else None
    )
    left = dfs(splitter_left)

    splitter_right_idx = bisect.bisect_left(col_idxs[y + 1], x)
    splitter_right = (
        (col_idxs[y + 1][splitter_right_idx], y + 1)
        if splitter_right_idx < len(col_idxs[y + 1])
        else None
    )
    right = dfs(splitter_right)

    visited[(x, y)] = left + right
    return visited[(x, y)]


part2 = dfs(first_splitter)

print("Part 1:", len(visited))
print("Part 2:", part2)
