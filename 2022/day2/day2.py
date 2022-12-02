import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = []

with open(file) as f:
    for line in f:
        a, b = line.strip().split()
        data.append((a, b))

part1 = 0
part2 = 0

for a, b in data:
    x = ord(a) - ord("A")
    y = ord(b) - ord("X")

    # Part 1
    if x == y:
        part1 += 3
    if (x + 1) % 3 == y:
        part1 += 6

    part1 += y + 1

    # Part 2
    if b == "X":
        part2 += (x + 2) % 3 + 1
    if b == "Y":
        part2 += x + 1
        part2 += 3
    if b == "Z":
        part2 += (x + 1) % 3 + 1
        part2 += 6

print(part1)
print(part2)
