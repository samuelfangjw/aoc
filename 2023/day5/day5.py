import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    sections = f.read().split("\n\n")
    seeds = [int(x) for x in sections[0].split()[1:]]
    seed_pairs = list(zip(seeds[0:len(seeds):2], seeds[1:len(seeds):2]))
    maps = [[[int(z) for z in y.split()] for y in x.splitlines()[1:]] for x in sections[1:]]
    
    for m in maps:
        m.sort(key=lambda x:x[1])
        m.append((0, float('inf'), 0))

part1, part2 = float('inf'), float('inf')

for seed in seeds:
    val = seed
    for m in maps:
        for dest, source, length in m:
            if source <= val < source + length:
                val = dest + (val-source)
                break
    part1 = min(val, part1)

for start, l in seed_pairs:
    r = [(start, start + l)]
    r2 = []

    for m in maps:
        for s, e in r:
            if s == e:
                for dest, source, length in m:
                    if source <= s < source + length:
                        s = dest + (s-source)
                        r2.append((s,s))
                        break
                continue
            while s < e:
                for dest, source, length in m:
                    if source <= s < source + length:
                        r2.append((dest+s-source, dest + min(e, source + length-1) - source))
                        s = source + length
                        break
                    elif source < s:
                        continue
                    else:
                        r2.append((s, min(e, source - 1)))
                        s = source
                        break
                        
        r = r2
        r2 = []

    part2 = min(min([x[0] for x in r]), part2)

print(part1, part2)
