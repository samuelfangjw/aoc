import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
rotations = []

with open(file) as f:
    for line in f:
        line = line.strip()
        steps = int(line[1:])
        rotations.append(("R" if line.startswith("R") else "L", steps))

curr_pos = 50
part1, part2 = 0, 0

for direction, steps in rotations:
    if direction == "R":
        part2 += (curr_pos + steps) // 100
        curr_pos = (curr_pos + steps) % 100
    else:
        part2 += ((100 - curr_pos) % 100 + steps) // 100
        curr_pos = (curr_pos - steps) % 100

    if curr_pos == 0:
        part1 += 1

print("Part 1:", part1)
print("Part 2:", part2)
