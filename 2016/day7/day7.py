import sys
import re

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = []

with open(file) as f:
    for line in f:
        line = line.strip()
        a = re.split('\[[a-z]*\]', line)
        b = re.findall('\[[a-z]*\]', line)
        b = [x[1:-1] for x in b]
        data.append((a,b))

part1 = 0
for x, y in data:
    possible = False
    for a in x:
        if any([True for i,j,k,l in zip(a[:-3], a[1:-2], a[2:-1], a[3:]) if i == l and j == k and i != j]):
            possible = True
            break
    for a in y:
        if any([True for i,j,k,l in zip(a[:-3], a[1:-2], a[2:-1], a[3:]) if i == l and j == k and i != j]):
            possible = False
            break
    if possible:
        part1 += 1

print(part1)

part2 = 0
for x, y in data:
    possible = []
    for a in x:
        possible += [j+i+j for i,j,k in zip(a[:-2], a[1:-1], a[2:]) if i == k and i != j]
    if possible:
        if any([any([p in yy for yy in y]) for p in possible]):
            part2 += 1

print(part2)
