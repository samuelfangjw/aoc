import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    input = []
    for line in f:
        line = line.strip().split("x")
        input.append([int(x) for x in line])

sides = [[a * b, b * c, a * c] for a,b,c in input]
part1 = sum((a + b + c) * 2 + min(a,b,c) for a, b, c in sides)
part2 = sum((a + b + c - max(a, b, c)) * 2 + a * b * c for a, b, c in input)

print(part1)
print(part2)
