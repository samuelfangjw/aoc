import sys


file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    ranges, ingredients = f.read().strip().split("\n\n")


ranges = sorted(
    [(int(a), int(b)) for line in ranges.split("\n") for a, b in [line.split("-")]]
)
ingredients = sorted([int(x) for x in ingredients.split("\n")])

range_index = 0
fresh_count = 0

for i in ingredients:
    # filter out ranges that end before i
    while range_index < len(ranges) and ranges[range_index][1] < i:
        range_index += 1

    # no more valid ranges
    if range_index == len(ranges):
        break

    # current range starts after i
    if ranges[range_index][0] > i:
        continue

    # i is valid
    fresh_count += 1

non_overlapping_ranges = []
for s, e in ranges:
    if not non_overlapping_ranges or non_overlapping_ranges[-1][1] < s:
        non_overlapping_ranges.append([s, e])
    else:
        non_overlapping_ranges[-1][1] = max(non_overlapping_ranges[-1][1], e)

valid_count = sum(e - s + 1 for s, e in non_overlapping_ranges)

print("Part 1:", fresh_count)
print("Part 2:", valid_count)
