import sys
import itertools

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
S = set()
H = dict()

with open(file) as f:
    for line in f:
        line = line.strip().split()
        a = line[0]
        op = line[2]
        n = int(line[3])
        b = line[10][:-1]
        if op == "lose":
            n = -n
        S.add(a)
        H[(a,b)] = n

def get_opt():
    perms = list(itertools.permutations(S))
    return max(sum(H[y] for y in zip(x[:-1], x[1:])) + 
        sum(H[y] for y in zip(x[1:], x[:-1])) + 
        H[(x[0], x[-1])] + H[(x[-1], x[0])]  for x in perms)

# Part 1
print(get_opt())

# Part 2
for x in S:
    H[(x, "You")] = 0
    H[("You", x)] = 0
S.add("You")

print(get_opt())

