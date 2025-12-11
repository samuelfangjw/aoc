from collections import defaultdict
from functools import cache
import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file, "r") as f:
    lines = [line.strip() for line in f.readlines()]


nodes = defaultdict(list)
for line in lines:
    raw = line.split(":")
    src = raw[0].strip()
    dsts = [d.strip() for d in raw[1].strip().split()]
    nodes[src].extend(dsts)


@cache
def dfs(node, end):
    if node == end:
        return 1

    res = 0
    for n in nodes[node]:
        res += dfs(n, end)

    return res


part1 = dfs("you", "out")

path1 = dfs("svr", "fft") * dfs("fft", "dac") * dfs("dac", "out")
path2 = dfs("svr", "dac") * dfs("dac", "fft") * dfs("fft", "out")
part2 = path1 + path2

print("Part 1:", part1)
print("Part 2:", part2)
