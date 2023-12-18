import sys
from collections import defaultdict

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = f.read().strip().split(',')

part1, part2 = 0, 0

boxes = defaultdict(list)

def get_hash(s):
    h = 0
    for c in s:
        h += ord(c)
        h *= 17
        h = h % 256
    return h

for s in data:
    part1 += get_hash(s)

    if '-' in s:
        lens = s[:-1]
        box = get_hash(lens)
        b = boxes[box]
        for i in range(len(b)):
            if b[i][0] == lens:
                b.pop(i)
                break

    if '=' in s:
        lens,focal = s.split('=')
        box = get_hash(lens)
        b = boxes[box]
        i = 0
        while i < len(b):
            if b[i][0] == lens:
                b[i] = (lens, focal)
                break
            i += 1
        if i == len(b):
            boxes[box].append((lens, focal))

for i in range(256):
    box = boxes[i]
    for j in range(len(box)):
        part2 += (i+1) * (j+1) * int(box[j][1])

print(part1, part2)
