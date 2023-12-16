import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
seqs = []

with open(file) as f:
    for line in f:
        line = line.strip()
        seqs.append(list(map(int,line.split())))

part1, part2 = 0, 0

for seq in seqs:
    hist = [] # first & last val of prev seq
    while len([x for x in seq if x != 0]) > 0:
        hist.append((seq[0], seq[-1]))
        seq = [b-a for a, b in zip(seq[0:-1], seq[1:])]

    prev, next = 0, 0
    for i in range(len(hist)-1, -1, -1):
        prev = hist[i][0] - prev
        next = hist[i][1] + next
    part1 += next
    part2 += prev

print(part1, part2)
