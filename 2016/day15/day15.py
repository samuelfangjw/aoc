import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = []

with open(file) as f:
    for line in f:
        line = line.strip().split()
        positions = int(line[3])
        initial = int(line[11][:-1])
        data.append((positions, initial))

def solve(discs):
    start = 1
    found = False
    while not found:
        found = True
        for i in range(len(discs)):
            if (start + discs[i][1] + i + 1) % discs[i][0] != 0:
                found = False
                break

        start += 1
    return start -1

part1, part2 = solve(data), solve(data + [(11, 0)])
print("Part 1:", part1)
print("Part 2:", part2)
