from ast import literal_eval
from functools import cmp_to_key
import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = f.read()


def check(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return 1
        elif a == b:
            return 0
        else:
            return -1
    elif isinstance(a, int):
        a = [a]
    elif isinstance(b, int):
        b = [b]

    m_len = min(len(a), len(b))
    for i in range(m_len):
        r = check(a[i], b[i])
        if r != 0:
            return r

    if len(a) < len(b):
        return 1
    elif len(a) == len(b):
        return 0
    else:
        return -1


pkts = []

# part 1
part1 = 0
for idx, pair in enumerate(data.split('\n\n')):
    a, b = map(literal_eval, pair.strip().split('\n'))
    pkts.extend([a, b])
    if check(a, b) == 1:
        part1 += idx + 1

print(part1)

# part 2
pkts.extend([[[2]], [[6]]])
pkts = sorted(pkts, key=cmp_to_key(check), reverse=True)
part2 = (pkts.index([[2]]) + 1) * (pkts.index([[6]]) + 1)

print(part2)
