import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    times, distance = f.read().strip().splitlines()
    times = times.split()[1:]
    distance = distance.split()[1:]
    
    records = []
    for i in range(4):
        records.append((int(times[i]), int(distance[i])))

    time2 = int("".join(times))
    dist2 = int("".join(distance))

# part 1
part1 = 1

for time, dist in records:
    start, end = 1, time
    while (time-start) * start <= dist:
        start += 1
    
    while (time-end) * end <= dist:
        end -= 1

    part1 *= end-start+1

# part 2
start, end = 1, time2
while (time2-start) * start <= dist2:
    start += 1

while (time2-end) * end <= dist2:
    end -= 1

part2 = end-start+1

print(part1, part2)
