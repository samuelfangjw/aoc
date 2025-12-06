import sys


file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file, "r") as f:
    commands = [int(x) for x in f.read().strip().splitlines()]


def part_one(commands):
    curr = 0
    steps = 0
    while curr < len(commands):
        steps += 1
        jump = commands[curr]
        commands[curr] += 1
        curr += jump
    return steps


def part_two(commands):
    curr = 0
    steps = 0
    while curr < len(commands):
        steps += 1
        jump = commands[curr]
        if jump >= 3:
            commands[curr] -= 1
        else:
            commands[curr] += 1
        curr += jump
    return steps


print("Part 1:", part_one(commands.copy()))
print("Part 2:", part_two(commands.copy()))
