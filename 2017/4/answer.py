import sys
from collections import Counter

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = []
    for line in f:
        line = line.strip().split()
        data.append(line)

part1 = sum([1 for row in data if Counter(row).most_common(1)[0][1] == 1])
data = [["".join(sorted(list(word))) for word in row] for row in data]
part2 = sum([1 for row in data if Counter(row).most_common(1)[0][1] == 1])

print("Part 1:", part1)
print("Part 2:", part2)
