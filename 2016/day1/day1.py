import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    for line in f:
        instructions = [(x[0], int(x[1:])) for x in line.strip().split(", ")]

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
facing = 0
pos = (0, 0)
visited = set([(0,0)])
FOUND = False

for x, y in instructions:
    if x == 'R':
        facing += 1
    else:
        facing -= 1
    facing = facing % 4

    if not FOUND:
        for _ in range(1, y + 1):
            pos = (pos[0] + 1 * dirs[facing][0], pos[1] + 1 * dirs[facing][1])
            if pos in visited:
                FOUND = True
                part2 = pos
            else:
                visited.add(pos)
    else:
        pos = (pos[0] + y * dirs[facing][0], pos[1] + y * dirs[facing][1])

print(sum(abs(x) for x in pos))
print(sum(abs(x) for x in part2))
