target = 29000000
size = 1000000
part1 = [0] * size
part2 = [0] * size

for i in range(1, size):
    count = 0
    for j in range(i, size, i):
        part1[j] += i * 10
        if count < 50:
            part2[j] += i * 11
        count += 1

for idx, n in enumerate(part1):
    if n >= target:
        print(idx)
        break

for idx, n in enumerate(part2):
    if n >= target:
        print(idx)
        break
    