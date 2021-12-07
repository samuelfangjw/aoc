import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    input = []
    for line in f:
        line = line.strip().split(",")
        input = [int(x) for x in line]

part1 = 10000000000
part2 = 10000000000

memo = {}

def calculate_cost(n):
    if n in memo:
        return memo[n]
    memo[n] = sum(list(range(n + 1)))
    return memo[n]

for i in range(min(input), max(input) + 1):
    part1 = min(sum([abs(x - i) for x in input]), part1)
    part2 = min(sum([calculate_cost(abs(x - i)) for x in input]), part2)

print(part1)
print(part2)