import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    input = []
    for line in f:
        line = int(line)
        input.append(line)

input.sort()

target = 150

def ways(n, k):
    if n < 0:
        return []
    if n == 0:
        return [0]
    if k == -1:
        return []
    
    a = ways(n - input[k], k - 1)
    b = ways(n, k-1)
    return [x + 1 for x in a] + b

valid = ways(150, len(input) - 1)
part1 = len(valid)
num = min(valid)
part2 = sum(1 for x in valid if x == num)
print(part1)
print(part2)
