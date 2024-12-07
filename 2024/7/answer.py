import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = []
    for line in f:
        line = line.strip().split()
        line[0] = line[0][:-1]
        data.append([int(x) for x in line])

part1, part2 = 0, 0

def recurse(rest, res, idx, curr):
    if curr > res:
        return [False, False]

    if idx == len(rest):
        if curr == res:
            return [True, True]
        return [False, False]
    
    x = recurse(rest, res, idx + 1, curr + rest[idx])
    y = recurse(rest, res, idx + 1, curr * rest[idx])
    z = recurse(rest, res, idx + 1, int(str(curr) + str(rest[idx])))
    return [x[0] or y[0], x[1] or y[1] or z[1]]

for line in data:
    res, curr, rest = line[0], line[1], line[2:]

    one, two = recurse(rest, res, 0, curr)
    if one:
        part1 += res
    if two:
        part2 += res

print("Part 1:", part1)
print("Part 2:", part2)
