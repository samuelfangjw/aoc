from functools import cache
import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = [int(x) for x in f.read().strip().split()]

@cache
def count(num, n):
    if n == 0:
        return 1
    
    if num == 0:
        return count(1, n - 1)
    elif len(str(num)) % 2 == 0:
        num_str = str(num)
        first_half = int(num_str[:len(num_str) // 2])
        second_half = int(num_str[len(num_str) // 2:])
        return count(first_half, n - 1) + count(second_half, n - 1)
    else:
        return count(num * 2024, n - 1)

print("Part 1:", sum(count(x, 25) for x in data))
print("Part 2:", sum(count(x, 75) for x in data))
