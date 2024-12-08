import sys
import itertools
from collections import defaultdict

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = []
    for line in f:
        line = line.strip()
        data.append(line)

R, C = len(data), len(data[0])

nodes = defaultdict(list)
for i in range(R):
    for j in range(C):
        if data[i][j] == '.':
            continue
        nodes[data[i][j]].append((i, j))

part1, part2 = 0, 0
one, two = set(), set()

def is_valid(x, y):
    return 0 <= x < R and 0 <= y < C

for n, ns in nodes.items():
    for (x1, y1), (x2, y2) in itertools.combinations(ns, 2):
        a, b = 0, 0
        pt_a, pt_b = (x1, y1), (x2, y2)
        dx, dy = x2 - x1, y2 - y1

        while is_valid(*pt_a):
            if a == 1:
                one.add(pt_a)
            two.add(pt_a)
            a += 1
            pt_a = (pt_a[0] - dx, pt_a[1] - dy)

        while is_valid(*pt_b):
            if b == 1:
                one.add(pt_b)
            two.add(pt_b)
            b += 1
            pt_b = (pt_b[0] + dx, pt_b[1] + dy)

print("Part 1:", len(one))
print("Part 2:", len(two))
