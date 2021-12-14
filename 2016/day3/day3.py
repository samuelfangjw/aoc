import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = []

with open(file) as f:
    for line in f:
        line = [int(x) for x in line.strip().split()]
        data.append(line)

part1 = 0
for t in data:
    if sum(t) > 2 * max(t):
        part1 += 1

part2 = 0
for i in range(0,len(data),3):
    for j in range(3):
        t = (data[i][j], data[i+1][j], data[i+2][j])
        if sum(t) > 2 * max(t):
            part2 += 1

print(part1)
print(part2)
