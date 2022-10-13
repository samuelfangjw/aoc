import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

n_rows = 6
n_cols = 50
commands = []
grid = [[0 for _ in range(n_cols)] for _ in range(n_rows)]

with open(file) as f:
    for line in f:
        line = line.strip()
        tokens = line.split()
        if tokens[0] == 'rotate':
            dimension = tokens[1]
            idx = tokens[2].split("=")[1]
            by = tokens[4]
            if dimension == 'column':
                commands.append((2, int(idx), int(by)))
            else:
                commands.append((1, int(idx), int(by)))
        else:
            w = tokens[1].split("x")[0]
            h = tokens[1].split("x")[1]
            commands.append((0, int(w), int(h)))

for c, a, b in commands:
    if c == 0:
        for i in range(a):
            for j in range(b):
                grid[j][i] = 1
    elif c == 1:
        # rotate row
        new_row = [0] * n_cols
        for idx in range(n_cols):
            new_idx = (idx + b) % n_cols
            new_row[new_idx] = grid[a][idx]
        grid[a] = new_row
    else:
        # rotate column
        new_column = [0] * n_rows
        for idx in range(n_rows):
            new_idx = (idx + b) % n_rows
            new_column[new_idx] = grid[idx][a]
        for idx in range(n_rows):
            grid[idx][a] = new_column[idx]

part1 = sum(sum(r) for r in grid)
print(part1)

# part 2
for r in grid:
    r = [" " if x == 0 else u"\u2588" for x in r]
    print("".join(r))
