from copy import deepcopy
import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = []
    for line in f:
        data.append(line.strip().split())

def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return  False

def solve(reg_a):
    instructions = deepcopy(data)
    idx = -1
    registers = {
        'a': reg_a,
        'b': 0,
        'c': 0,
        'd': 0
    }

    while idx < len(instructions) - 1:
        idx += 1
        tokens = instructions[idx]
        op = tokens[0]

        if idx == 5:
            registers["a"] += registers["c"] * registers["d"]
            registers["c"] = 0
            registers["d"] = 0
            idx = 9
        elif op == "cpy":
            val = tokens[1]
            reg = tokens[2]

            if (is_digit(reg)):
                continue

            if is_digit(val):
                registers[reg] = int(val)
            else:
                registers[reg] = registers[val]
        elif op == "inc":
            reg = tokens[1]

            if is_digit(reg):
                continue

            registers[reg] += 1
        elif op == "dec":
            reg = tokens[1]

            if is_digit(reg):
                continue

            registers[reg] -= 1
        elif op == "tgl":
            reg = tokens[1]
            if is_digit(reg):
                offset = int(reg)
            else:
                offset = registers[reg]
            
            target = idx + int(offset)
            if target >= len(instructions) or target < 0:
                continue

            if len(instructions[target]) == 2:
                if instructions[target][0] == "inc":
                    instructions[target][0] = "dec"
                else:
                    instructions[target][0] = "inc"
            else:
                if instructions[target][0] == "jnz":
                    instructions[target][0] = "cpy"
                else:
                    instructions[target][0] = "jnz"
        else: # jnz
            reg = tokens[1]
            offset = tokens[2]

            if is_digit(offset):
                offset = int(offset)
            else:
                offset = registers[offset]

            if is_digit(reg):
                if reg != "0":
                    idx = idx + offset - 1
            else:
                if registers[reg] != 0:
                    idx = idx + offset - 1

    return registers

part1, part2 = solve(7)["a"], solve(12)["a"]
print("Part 1:", part1)
print("Part 2:", part2)
