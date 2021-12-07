import sys
from collections import defaultdict

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    input = []
    for line in f:
        line = line.strip().split()
        name = line[0]
        speed = int(line[3])
        time = int(line[6])
        rest = int(line[13])
        input.append([name, speed, time, rest])

S = 2503

# Part 1
part1 = max((S // (rest + time)) * (speed * time) + min(S % (rest + time), time) * speed for _, speed, time, rest in input)
print(part1)

# Part 2
PTS = defaultdict(int)
for i in range(1, S + 1):
    highest = 0
    winners = []
    for name, speed, time, rest in input:
        curr = (i // (rest + time)) * (speed * time) + min(i % (rest + time), time) * speed
        if curr > highest:
            highest = curr
            winners = [name]
        elif curr == highest:
            winners.append(name)
    for w in winners:
        PTS[w] += 1

part2 = max(PTS.values())
print(part2)