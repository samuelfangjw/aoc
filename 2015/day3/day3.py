import sys
from collections import defaultdict

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

D = {"<": (-1, 0), ">": (1, 0), "^": (0, 1), "v": (0, -1)}

with open(file) as f:
    line = f.readline().strip()
    input = line

def part1():
    H = defaultdict(int)
    s = (0,0)
    H[s] += 1
    for x in input:
        s  = (s[0] + D[x][0], s[1] + D[x][1])
        H[s] += 1
    return len(H)

def part2():
    H = defaultdict(int)
    s = (0,0)
    r = (0,0)
    H[s] += 2
    for x in input[::2]:
        s  = (s[0] + D[x][0], s[1] + D[x][1])
        H[s] += 1
    for x in input[1::2]:
        r  = (r[0] + D[x][0], r[1] + D[x][1])
        H[r] += 1
    return len(H)

print(part1())
print(part2())