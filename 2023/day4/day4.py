import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = []

with open(file) as f:
    for line in f:
        line = line.strip().split(": ")[1]
        line = [x.split() for x in line.split(" | ")]
        data.append(line)

part1, part2 = 0, 0
counts = [1 for _ in data]

for idx, (winning, actual) in enumerate(data):
    count = 0

    for num in actual:
        if num in winning:
            count += 1

    if count:
        part1 += pow(2, count-1)
        for x in range(idx+1, idx + count + 1):
            counts[x] += counts[idx]

part2 = sum(counts)
print(part1, part2)
