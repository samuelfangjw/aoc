import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = []
    for line in f:
        line = line.strip().split("-")
        data.append((int(line[0]), int(line[1])))

data.sort(key=lambda x: x[1])
data.sort(key=lambda x: x[0])

ips = [data[0]]
for i in range(1, len(data)):
    if ips[-1][1] + 1 >= data[i][0]:
        ips[-1] = (ips[-1][0], max(ips[-1][1], data[i][1]))
    else:
        ips.append(data[i])

part1 = ips[0][1] + 1
part2 = 0

for i in range(len(ips) - 1):
    part2 += ips[i+1][0] - ips[i][1] - 1

print("Part 1:", part1)
print("Part 2:", part2)
