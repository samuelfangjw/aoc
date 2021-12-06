import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    input = []
    for line in f:
        line = line.strip().split(",")
        input = line
        input = [int(x) for x in input]

def count_fish(days):
    fishes8 = [0] * (days + 1)
    fishes6 = [0] * (days + 1)
    count = len(input) * 2

    for x in input:
        fishes6[x + 1] += 1
        fishes8[x + 1] += 1

    for i in range(days + 1):
        num = fishes8[i]
        if i + 9 <= days:
            fishes8[i + 9] += num
            fishes6[i + 9] += num
            count += num

        num = fishes6[i]
        if i + 7 <= days:
            fishes8[i + 7] += num
            fishes6[i + 7] += num
            count += num
    
    return count

part1 = count_fish(80)
part2 = count_fish(256)
print(part1)
print(part2)
