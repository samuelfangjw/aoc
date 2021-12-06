import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    input = []
    for line in f:
        line = line.strip()
        input = line

part1 = sum([1 if x == "(" else -1 for x in input])

floor = 0
for idx, x in enumerate(input):
    if x == "(":
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        part2 = idx + 1
        break

print(part1)
print(part2)