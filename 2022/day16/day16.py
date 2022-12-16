from collections import deque
from functools import cache
import sys
from bitsets import bitset
from parse import compile

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = f.read()

p = compile('Valve {} has flow rate={:d}; tunnels lead to valves {}')

capacity = {}
tunnels = {}
possible = []

for line in data.splitlines():
    r = p.parse(line.replace(
        'tunnel leads to valve', 'tunnels lead to valves'))
    v = r[0]
    c = r[1]
    to = r[2].replace(',', '').split()

    tunnels[v] = to
    if c > 0:
        capacity[v] = c
        possible.append(v)

dist = {}
possible.append('AA')

for v in possible:
    seen = set()
    q = deque([(v, 0)])
    while q:
        n1, d = q.popleft()
        if n1 in seen:
            continue
        seen.add(n1)
        if n1 in possible and n1 != 'AA':
            dist[(v, n1)] = d
        for n2 in tunnels[n1]:
            if n2 not in seen:
                q.append((n2, d + 1))

possible.remove('AA')
valves = bitset('Valves', tuple(possible))


@cache
def dfs(v1, left, bits, valves):
    opened = valves.fromint(bits)

    if left <= 1 or opened == valves.supremum:
        return 0

    curr = 0
    if v1 != 'AA':
        opened = opened.union(valves([v1]))

    for v2 in valves.supremum.difference(opened):
        d = dist[(v1, v2)]
        if left - d - 1 >= 1:
            curr = max(curr, dfs(v2, left-d-1, opened, valves) +
                       capacity[v2] * (left - d - 1))

    return curr


part1 = dfs('AA', 30, valves([]), valves)
print(part1)

part2 = 0
for i in range(int(valves.supremum) + 1):
    a = tuple(valves.fromint(i).members())
    b = tuple(valves.supremum.difference(a).members())
    if len(a) != 0 and len(b) != 0:
        part2 = max(part2, dfs('AA', 26, valves([]), bitset(
            'Valves', a)) + dfs('AA', 26, valves([]), bitset('Valves', b)))

print(part2)
