from collections import defaultdict
import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    grid = f.read().splitlines()

R = len(grid)
C = len(grid[0])

d = [(r, c) for r in (0, -1, 1) for c in (0, -1, 1) if not (r == 0 and c == 0)]
n = [(r, c) for r, c in d if r == -1]
s = [(r, c) for r, c in d if r == 1]
w = [(r, c) for r, c in d if c == -1]
e = [(r, c) for r, c in d if c == 1]

f = [lambda r, c, elves: all((r+dr, c+dc) not in elves for dr, dc in n), lambda r, c, elves: all((r+dr, c+dc) not in elves for dr, dc in s),
     lambda r, c, elves: all((r+dr, c+dc) not in elves for dr, dc in w), lambda r, c, elves: all((r+dr, c+dc) not in elves for dr, dc in e)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

elves = []
elvesset = set()
for r in range(R):
    for c in range(C):
        if grid[r][c] == '#':
            elves.append((r, c))
            elvesset.add((r, c))

newelves = [None] * len(elves)
round = 0
while True:
    proposed = defaultdict(int)

    for idx in range(len(elves)):
        r, c = elves[idx]
        newelves[idx] = None
        if all((r+dr, c + dc) not in elvesset for dr, dc in d):
            continue

        for i in range(4):
            x = (round + i) % 4

            if f[x](r, c, elvesset):
                dr, dc = move[x]
                proposed[(r+dr, c+dc)] += 1
                newelves[idx] = (r+dr, c+dc)
                break

    found = False
    for idx in range(len(elves)):
        if proposed[newelves[idx]] == 1:
            found = True
            elvesset.remove(elves[idx])
            elves[idx] = newelves[idx]
            elvesset.add(elves[idx])

    if not found:
        part2 = round + 1
        print(part2)
        break

    if round == 10 - 1:
        minr, minc = 1000, 1000
        maxr, maxc = -1000, -1000
        for r, c in elves:
            minr, minc = min(minr, r), min(minc, c)
            maxr, maxc = max(maxr, r), max(maxc, c)

        area = (maxr-minr+1) * (maxc-minc+1)
        part1 = area - len(elves)
        print(part1)

    round += 1
