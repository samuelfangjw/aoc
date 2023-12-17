import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
grid = []

with open(file) as f:
    for line in f:
        line = list(line.strip())
        grid.append(line)

def solve(size):
    galaxies = []
    empty_rows = 0
    for r in range(len(grid)):
        is_empty = True
        for c in range(len(grid[0])):
            if grid[r][c] == "#":
                galaxies.append((r+empty_rows,c))
                is_empty = False
        if is_empty:
            empty_rows += size - 1

    galaxies.sort(key=lambda x: x[1])
    prev = -1
    empty_cols = 0
    for idx in range(len(galaxies)):
        r,c = galaxies[idx]

        if c > prev + 1:
            empty_cols += (c - prev - 1) * (size - 1)
            
        prev = c
        galaxies[idx] = (r, c+empty_cols)

    ans = 0
    for x in range(len(galaxies)-1):
        for y in range(x+1, len(galaxies)):
            r1,c1 = galaxies[x]
            r2,c2 = galaxies[y]
            ans += abs(r1-r2) + abs(c1-c2)
    return ans

part1, part2 = solve(2), solve(1000000)
print(part1, part2)
