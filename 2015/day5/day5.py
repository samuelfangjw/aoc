import sys
import re

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    input = []
    for line in f:
        line = line.strip()
        input.append(line)

banned = ["ab", "cd", "pq", "xy"]
def test(line):
    c1 = len(re.findall("[aeiou]", line)) >= 3
    c2 = any(x == y for x,y in list(zip(line[:-1], line[1:])))
    c3 = any(x + y in banned for x, y in list(zip(line[:-1], line[1:])))
    return c1 and c2 and not c3

part1 = len([x for x in input if test(x)])
print(part1)

def test2(line):
    c1 = any(x == y for x,y in list(zip(line[:-2], line[2:])))
    l = [line[i:i+2] for i in range(0, len(line)) if i+2 <= len(line)]
    c2 = False
    for i in range(len(l)):
        if l[i] in l[:max(i-1, 0)] or l[i] in l[min(i+2, len(line)):]:
            c2 = True
            break
    return c1 and c2

part2 = len([x for x in input if test2(x)])
print(part2)
