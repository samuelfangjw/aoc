import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = f.read()

elves = [sum([int(x) for x in l.split()]) for l in data.split("\n\n")]
elves.sort(reverse=True)

print(elves[0])  # part 1
print(elves[0] + elves[1] + elves[2])  # part 2
