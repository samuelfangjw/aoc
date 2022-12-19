from collections import deque
import sys
from parse import compile

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = f.read().strip()

p = compile('Blueprint {:d}: Each ore robot costs {:d} ore. Each clay robot costs {:d} ore. Each obsidian robot costs {:d} ore and {:d} clay. Each geode robot costs {:d} ore and {:d} obsidian.')
blueprints = {}

for line in data.splitlines():
    r = p.parse(line)
    blueprints[r[0]] = (r[1], r[2], r[3], r[4], r[5], r[6])


def solve(idx, mins):
    (ore, clay, obsore, obsclay, geodeore, geodeobsidian) = blueprints[idx]
    maxsofar = 0
    queue = deque()
    # ore, clay, obsidian, open-geodes
    queue.append((mins, (1, 0, 0, 0), (0, 0, 0, 0)))
    seen = set()
    maxore = max(obsore, ore, clay, geodeore)

    while queue:
        m, (o, c, ob, g), (om, cm, obm, gm) = queue.popleft()

        om = min(maxore * (m+1), om)
        cm = min(obsclay * (m+1), cm)
        obm = min(geodeobsidian * (m+1), obm)

        if (m, o, c, ob, g, om, cm, obm, gm) in seen:
            continue
        else:
            seen.add((m, o, c, ob, g, om, cm, obm, gm))

        maxsofar = max(maxsofar, gm)
        if gm + g * m + m * (m + 1) // 2 < maxsofar:
            continue

        if m == 0:
            continue

        build = (om >= ore, om >= clay, om >= obsore and cm >=
                 obsclay, om >= geodeore and obm >= geodeobsidian)

        if build[3]:
            # always build geode bots
            queue.append((m - 1, (o, c, ob, g+1),
                         (om+o-geodeore, cm+c, obm+ob-geodeobsidian, gm+g)))
        else:
            # build ore bot
            if build[0] and maxore * m >= om:
                queue.append((m - 1, (o+1, c, ob, g),
                             (om+o-ore, cm+c, obm+ob, gm+g)))
            # build clay bot
            if build[1] and obsclay * m >= cm:
                queue.append((m - 1, (o, c+1, ob, g),
                             (om+o-clay, cm+c, obm+ob, gm+g)))
            # build obsidian bot
            if build[2] and geodeobsidian * m >= obm:
                queue.append((m - 1, (o, c, ob+1, g),
                             (om+o-obsore, cm+c-obsclay, obm+ob, gm+g)))
            # skip building bot
            if not all(build):
                queue.append((m - 1, (o, c, ob, g),
                              (om+o, cm+c, obm+ob, gm+g)))

    return maxsofar


# Unoptimized brute force solution
# Runs in 9-10 mins
part1 = 0
part2 = 1
for idx in blueprints.keys():
    t = solve(idx, 24)
    part1 += t * idx
    # print(idx, t)
    if idx <= 3:
        part2 *= solve(idx, 32)
        # print(part2)

print("Part 1:", part1)
print("Part 2:", part2)
