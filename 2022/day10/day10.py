import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = []

with open(file) as f:
    for line in f:
        line = line.strip()
        data.append(line)

cycle = 0
idx = -1
reg = 1
check = [20, 60, 100, 140, 180, 220]

program = []

for l in data:
    if l == "noop":
        program.append(l)
    else:
        program.append("noop")
        program.append(int(l.split()[1]))

part1 = 0
part2 = [' '] * 40 * 6

while cycle < 240:
    cycle += 1
    idx += 1

    if cycle in check:
        part1 += reg * cycle

    if abs(reg - (idx % 40)) <= 1:
        part2[idx] = u'\u2588'

    if program[idx % len(program)] != "noop":
        reg += program[idx % len(program)]


print(part1)

for i in range(0, 40 * 6, 40):
    print("".join(part2[i:i+40]))
