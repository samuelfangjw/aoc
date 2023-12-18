import sys
from functools import cache

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
springs = []

with open(file) as f:
    for line in f:
        x, y = line.strip().split()
        y = tuple([int(z) for z in y.split(",")])
        springs.append((x,y))

@cache
def ways(mpos, gpos, mapping, groups):
    if mpos >= len(mapping) and gpos >= len(groups):
        return 1
    
    if mpos >= len(mapping):
        return 0

    if mapping[mpos] == '.':
        return ways(mpos+1, gpos, mapping, groups)

    if gpos >= len(groups):
        if mapping[mpos] == '#':
            return 0
        else:
            return ways(mpos+1, gpos, mapping, groups)

    ans = 0
    g = groups[gpos]
    if mpos + g < len(mapping):
        possible = True    
        
        for i in range(mpos, mpos + g):
            if mapping[i] == '.':
                possible = False
        
        if mapping[mpos + g] == '#':
            possible = False
        
        if possible:
            ans += ways(mpos + g + 1, gpos + 1, mapping, groups)
    
    if mapping[mpos] != '#':
        ans += ways(mpos + 1, gpos, mapping, groups)

    return ans

part1, part2 = 0, 0
for m, g in springs:
    part1 += ways(0, 0, m + '.', g)
    part2 += ways(0, 0, ((m + '?') * 5)[:-1] + '.', g * 5)

print(part1, part2)
