import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

part1, part2 = 0, 0

with open(file) as f:
    data = []
    for line in f:
        line = line.strip()
        data.append(line)

# Part 1
for i in range(len(data)):
    for j in range(len(data[0]) - 3):
        xs = data[i][j:j+4]
        if xs in ["XMAS", "SAMX"]:
            part1 += 1

for i in range(len(data) - 3):
    for j in range(len(data[0])):
        xs = data[i][j] + data[i+1][j] + data[i+2][j] + data[i+3][j]
        if xs in ["XMAS", "SAMX"]:
            part1 += 1

for i in range(len(data)-3):
    for j in range(len(data[0])-3):
        xs = data[i][j] + data[i+1][j+1] + data[i+2][j+2] + data[i+3][j+3]
        if xs in ["XMAS", "SAMX"]:
            part1 += 1

for i in range(len(data)-3):
    for j in range(len(data[0])-3):
        xs = data[i+3][j] + data[i+2][j+1] + data[i+1][j+2] + data[i][j+3]
        if xs in ["XMAS", "SAMX"]:
            part1 += 1

# Part 2
for i in range(len(data) - 2):
    for j in range(len(data[0]) - 2):
        xs = data[i][j] + data[i+1][j+1] + data[i+2][j+2]
        zs = data[i+2][j] + data[i+1][j+1] + data[i][j+2]
        if xs in ["MAS", "SAM"] and zs in ["MAS", "SAM"]:
            part2 += 1

print("Part 1:", part1)
print("Part 2:", part2)
