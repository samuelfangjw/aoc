import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = []
    for line in f:
        line = line.strip().split()
        data.append([int(x) for x in line])

part1, part2 = 0, 0

def is_safe(row):
    acceptable_vals = [1, 2, 3] if row[1] > row[0] else [-1, -2, -3]
    
    for i in range(len(row)-1):
        if row[i+1] - row[i] not in acceptable_vals:
            return False
    
    return True

for row in data:
    if is_safe(row):
        part1 += 1
        part2 += 1
    elif any([is_safe(row[:i] + row[i+1:]) for i in range(len(row))]):
        part2 += 1

print("Part 1:", part1)
print("Part 2:", part2)
