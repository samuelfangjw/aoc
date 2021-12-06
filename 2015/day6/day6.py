import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    input = []
    for line in f:
        line = line.strip().split()
        if "toggle" in line:
            type = 2
            coords = line[1].split(",") + line[3].split(",")
            coords = [int(x) for x in coords]
        else:
            type = 1 if line[1] == "off" else 0
            coords = line[2].split(",") + line[4].split(",")
            coords = [int(x) for x in coords]

        input.append([type, coords])

# Part 1
G1 = [[False for _ in range(1000)] for _ in range(1000)]

for type, (x1, y1, x2, y2) in input:
    x = min(x1, x2)
    y = min(y1, y2)
    for i in range(abs(x1 - x2) + 1):
        for j in range(abs(y1 - y2) + 1):
            if type == 0:
                G1[x + i][y + j] = True
            elif type == 1:
                G1[x + i][y + j] = False
            else:
                G1[x + i][y + j] = not G1[x + i][y + j]

part1 = sum(sum([1 if x else 0 for x in row]) for row in G1)
print(part1)

# Part 2
G2 = [[0 for _ in range(1000)] for _ in range(1000)]

for type, (x1, y1, x2, y2) in input:
    x = min(x1, x2)
    y = min(y1, y2)
    for i in range(abs(x1 - x2) + 1):
        for j in range(abs(y1 - y2) + 1):
            if type == 0:
                G2[x + i][y + j] += 1
            elif type == 1:
                G2[x + i][y + j] = max(0, G2[x + i][y + j] - 1)
            else:
                G2[x + i][y + j] += 2

part2 = sum(sum([x for x in row]) for row in G2)
print(part2)