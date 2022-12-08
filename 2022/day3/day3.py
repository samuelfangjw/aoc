import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = []

with open(file) as f:
    for line in f:
        line = line.strip()
        data.append(line)


def to_score(item):
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27


part1 = 0
for l in data:
    left = l[:len(l) // 2]
    right = l[len(l) // 2:]
    common = list(set(left).intersection(set(right)))[0]
    part1 += to_score(common)

part2 = 0
for idx in range(0, len(data), 3):
    a, b, c = data[idx: idx + 3]
    common = list(set(a).intersection(set(b)).intersection(set(c)))[0]
    part2 += to_score(common)

print(part1)
print(part2)
