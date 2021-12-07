import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    input = []
    for line in f:
        line = line.strip().replace(",", " ").replace(":", "").split()[2:]
        line = list(zip(line[::2], line[1::2]))
        S = {}
        for x in line:
            S[x[0]] = int(x[1])
        input.append(S)

C = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

# Part 1
for idx, x in enumerate(input):
    correct = True
    for y in x.keys():
        if C[y] != x[y]:
            correct = False
            break
    if correct:
        part1 = idx + 1
        break

# Part 2
for idx, x in enumerate(input):
    correct = True
    for y in x.keys():
        if y == "cats" or y == "trees":
            if C[y] >= x[y]:
                correct = False
                break
        elif y == "pomeranians" or y == "goldfish":
            if C[y] <= x[y]:
                correct = False
                break
        else:
            if C[y] != x[y]:
                correct = False
                break
    if correct:
        part2 = idx + 1
        break

print(part1)
print(part2)