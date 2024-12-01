import sys
from collections import Counter

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    left = []
    right = []
    for line in f:
        line = line.strip().split()
        left.append(int(line[0]))
        right.append(int(line[1]))

left.sort()
right.sort()

c = Counter(right)
part1, part2 = 0, 0

for i in range(len(left)):
    part1 += abs(left[i] - right[i])
    part2 += left[i] * c[left[i]]
    
print("Part 1:", part1)
print("Part 2:", part2)
