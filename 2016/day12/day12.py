from curses.ascii import isdigit
import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
contents = open(file).read()

lines = contents.splitlines()

def solve(reg_c):
    idx = 0
    registers = {
        'a': 0,
        'b': 0,
        'c': reg_c,
        'd': 0
    }
    while idx < len(lines):
        line = lines[idx].strip()
        tokens = line.split()
        op = tokens[0]
        if op == "cpy":
            val = tokens[1]
            reg = tokens[2]
            if isdigit(val[0]):
                registers[reg] = int(val)
            else:
                registers[reg] = registers[val]
        elif op == "inc":
            reg = tokens[1]
            registers[reg] += 1
        elif op == "dec":
            reg = tokens[1]
            registers[reg] -= 1
        else:
            reg = tokens[1]
            offset = int(tokens[2])
            if isdigit(reg[0]):
                if reg != "0":
                    idx = idx + offset - 1
            else:
                if registers[reg] != 0:
                    idx = idx + offset - 1
        idx += 1
    return registers

part1 = solve(0)["a"]
print(part1)

part2 = solve(1)["a"]
print(part2)
