import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = f.readline().strip()

for idx in range(len(data)):
    if len(set(data[idx:idx+4])) == 4:
        break

part1 = idx + 4

for idx in range(len(data)):
    if len(set(data[idx:idx+14])) == 14:
        break

part2 = idx + 14

print(part1)
print(part2)
