from functools import cache
import hashlib
import sys
import re
from collections import defaultdict, deque

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    salt = f.read().strip()

md5 = lambda x: hashlib.md5(x.encode()).hexdigest().lower()
three = lambda x: re.findall(r'(.)\1\1', x)
five = lambda x: set(re.findall(r'(.)\1\1\1\1', x))

@cache
def modified_md5(x):
    for _ in range(2017):
        x = md5(x)
    return x

def solve(hashing_fn):
    fives = defaultdict(deque)
    i, j = 0, 1000
    keys = 0

    for jj in range(1, j+1):
        s = hashing_fn(salt + str(jj))
        f = five(s)
        for x in f:
            fives[x].append(jj)

    while True:
        s = hashing_fn(salt + str(i))
        t = three(s)
        if t:
            x = t[0]
            d = fives[x]
            while d and d[0] <= i:
                d.popleft()
            if d:
                keys += 1

        if keys == 64:
            return i

        i += 1
        j += 1

        s = hashing_fn(salt + str(j))
        f = five(s)
        for x in f:
            fives[x].append(j)

part1, part2 = solve(md5), solve(modified_md5)

print("Part 1:", part1)
print("Part 2:", part2)
