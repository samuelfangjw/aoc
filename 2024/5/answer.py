from functools import cmp_to_key
import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    [section1, section2] = f.read().split("\n\n")

    rules, pages_list = set(), []
    for line in section1.splitlines():
        line = line.strip().split("|")
        rules.add(tuple([int(x) for x in line]))
    
    for line in section2.splitlines():
        line = line.strip().split(",")
        pages_list.append([int(x) for x in line])

def cmp(a, b):
    if (a, b) in rules:
        return -1
    elif (b, a) in rules:
        return 1
    else:
        return 0

part1, part2 = 0, 0
for pages in pages_list:
    is_valid = True
    for x, y in list(rules):
        if x in pages and y in pages and pages.index(x) > pages.index(y):
            is_valid = False
            break
    
    if is_valid:
       part1 += pages[len(pages) // 2]
       continue

    pages.sort(key=cmp_to_key(cmp))
    part2 += pages[len(pages) // 2]

print("Part 1:", part1)
print("Part 2:", part2)
