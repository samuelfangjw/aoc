import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = []

with open(file) as f:
    for line in f:
        line = line.strip()
        data.append(line)

data = [l.split(',') for l in data]

part1 = 0
for a, b in data:
    astart, aend = map(int, a.split('-'))
    bstart, bend = map(int, b.split('-'))

    if (astart <= bstart and aend >= bend) or (bstart <= astart and bend >= aend):
        part1 += 1

part2 = 0
for a, b in data:
    astart, aend = map(int, a.split('-'))
    bstart, bend = map(int, b.split('-'))

    if (astart <= bstart and aend >= bend) or (bstart <= astart and bend >= aend):
        part2 += 1
    elif (bstart <= aend and bend >= aend) or (astart <= bend and aend >= bend):
        part2 += 1

print(part1)
print(part2)
