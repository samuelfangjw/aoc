import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = f.read().strip()

def solve(skip):
    count = 0
    for idx, x in enumerate(data):
        if x == data[(idx + skip) % len(data)]:
            count += int(x)
    return count
    
print("Part 1:", solve(1))
print("Part 2:", solve(len(data) // 2))
