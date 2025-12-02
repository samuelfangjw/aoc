import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    ranges = []
    for part in f.read().strip().split(","):
        start, end = map(int, part.split("-"))
        ranges.append((start, end))


def has_equal_half(s):
    mid = len(s) // 2
    return s[:mid] == s[mid:]


def has_repeated_pattern(s):
    n = len(s)
    for length in range(1, n // 2 + 1):
        if n % length == 0:
            pattern = s[:length]
            if pattern * (n // length) == s:
                return True
    return False


part1, part2 = 0, 0
for start, end in ranges:
    for x in range(start, end + 1):
        x_str = str(x)

        if has_equal_half(x_str):
            part1 += x

        if has_repeated_pattern(x_str):
            part2 += x

print("Part 1:", part1)
print("Part 2:", part2)
