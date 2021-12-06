import sys
import itertools

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    G = {}
    C = set()

    for line in f:
        line = line.strip().split(" = ")
        a, b = line[0].split(" to ")
        dist = int(line[1])
        C.add(a)
        C.add(b)
        G[(a, b)] = dist
        G[(b, a)] = dist

routes = list(itertools.permutations(C))

def get_dist(route):
    paths = list(zip(route[:-1], route[1:]))    
    return sum(G[x] for x in paths)

dist = [get_dist(x) for x in routes]
part1 = min(dist)
part2 = max(dist)

print(part1)
print(part2)
