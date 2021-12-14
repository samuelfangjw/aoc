import sys
from collections import Counter

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = []

with open(file) as f:
    for line in f:
        line = line.strip()
        data.append((line[:-7], line[-7:][1:-1]))

part1 = 0
rooms = {}
for l, cs in data:
    a = Counter(l.replace('-', "")[:-3])
    a = sorted(sorted(a), key=a.get, reverse=True)[:5]
    if "".join(sorted(cs)) == "".join(sorted(a)):
        part1 += int(l[-3:])
        rooms[''.join([chr((ord(x) - ord('a') + int(l[-3:])) % 26 + ord('a')) if x != '-' else ' ' for x in l[:-3]])] = l[-3:]

print(part1)
for room in rooms:
    if 'north' in room:
        print(room, rooms[room])
