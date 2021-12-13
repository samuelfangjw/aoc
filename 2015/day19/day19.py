import sys
import re
from collections import defaultdict

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
R = defaultdict(list)

with open(file) as f:
    for line in f:
        line = line.strip()
        if line:
            line = line.split(" => ")
            if len(line) == 2:
                a,b = line
                R[a].append(b)
            else:
                M = line[0]

def part1(M):
    D = set()
    for i in range(len(M)):
        x = M[i:]
        for y in R.keys():
            for z in R[y]:
                if x.startswith(y):
                    D.add(M[:i] + x.replace(y, z, 1))
    print(len(D))

def part2(M):
    ans = sum([len(re.findall(x, M)) for x in R.keys()]) - len(re.findall('Y', M)) - 1
    print(ans)

part1(M)
part2(M)
