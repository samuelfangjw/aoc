from functools import cache
import sys
from collections import defaultdict

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = []

with open(file) as f:
    for line in f:
        line = line.strip()
        line = line.strip().split()
        data.append(line)

cd = ['/']
files = defaultdict(dict)
dirs = defaultdict(set)
alldirs = set()

for tokens in data:
    cmd = tokens[0]
    if tokens[0] == "$":
        if tokens[1] == "cd":
            if tokens[2] == '/':
                cd = ['/']
            elif tokens[2] == '..':
                cd = cd[:-1]
            else:
                cd.append(tokens[2])
                dirs["/".join(cd[:-1])].add("/".join(cd))
                alldirs.add("/".join(cd))
    else:
        a, b = tokens
        if a == 'dir':
            dirs["/".join(cd)].add(b)
            alldirs.add("/".join(cd))
        else:
            files["/".join(cd)][b] = int(a)


@cache
def get_size(dir):
    filesizes = sum(files[dir].values())
    nestedsizes = 0
    for d in dirs[dir]:
        nestedsizes += get_size(d)
    return filesizes + nestedsizes


dirsize = [get_size(d) for d in alldirs]
part1 = sum([s for s in dirsize if s <= 100000])

target = get_size('/') - 40000000
dirsize.sort()
for d in dirsize:
    if d >= target:
        part2 = d
        break

print(part1)
print(part2)
