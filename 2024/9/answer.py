import sys
from collections import defaultdict

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    line = list(int(x) for x in f.readline().strip())

part1, part2 = 0, 0

# Part 1
i, j = 0, len(line) - 1 if len(line) % 2 == 1 else len(line) - 2

count = [x for x in line]

idx = 0
while i <= j:
    if count[i] == 0:
        i += 1
        continue
    if count[j] == 0:
        j -= 2
        continue

    if i % 2 == 0:
        part1 += i // 2 * idx
        count[i] -= 1
    else:
        part1 += j // 2 * idx
        count[j] -= 1
        count[i] -= 1

    idx += 1

# Part 2
gaps = defaultdict(list)
removed = set()

for j in range(len(line) - 1 if len(line) % 2 == 1 else len(line) - 2, -1, -2):
    for i in range(1, j, 2):
        if line[i] >= line[j]:
            gaps[i].append(j)
            line[i] -= line[j]
            removed.add(j)
            break

idx = 0
for i in range(len(line)):
    if i % 2 == 1:
        for x in gaps[i]:
            for j in range(line[x]):
                part2 += x // 2 * idx
                idx += 1
        for j in range(line[i]):
            idx += 1
    else:
        if i in removed:
            for j in range(line[i]):
               idx += 1
        else:
            for j in range(line[i]):
                part2 += i // 2 * idx
                idx += 1

print("Part 1:", part1)
print("Part 2:", part2)
