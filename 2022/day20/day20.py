import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

items = []
with open(file) as f:
    for idx, e in enumerate(map(int, f.read().strip().splitlines())):
        items.append((idx, e))
        if e == 0:
            zerokey = (idx, e)


def solve(items, n):
    itemsfinal = items[:]
    for _ in range(n):
        for idx, e in items:
            removeidx = itemsfinal.index((idx, e))
            del itemsfinal[removeidx]
            newidx = (removeidx + e) % len(itemsfinal)
            if newidx == 0:
                newidx = len(itemsfinal)
            itemsfinal.insert(newidx, (idx, e))

    zeroidx = itemsfinal.index(zerokey)
    return sum([itemsfinal[(zeroidx + x) % len(itemsfinal)][1]
                for x in [1000, 2000, 3000]])


part1 = solve(items, 1)
print(part1)

part2 = solve([(idx, e * 811589153) for idx, e in items], 10)
print(part2)
