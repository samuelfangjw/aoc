import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file, "r") as f:
    regions = f.read().split("\n\n")[-1].splitlines()


count = 0
for region in regions:
    raw = region.split(":")
    x, y = raw[0].split("x")
    area = int(x) * int(y)

    shapes = [int(x) for x in raw[1].strip().split()]
    count += sum(shapes) * 9 <= area

print("Part 1:", count)
