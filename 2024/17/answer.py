import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    for idx, line in enumerate(f.readlines()):
        if idx == 0:
            A = int(line.split()[-1])
        elif idx == 1:
            B = int(line.split()[-1])
        elif idx == 2:
            C = int(line.split()[-1])
        elif idx == 4:
            program_str = line.split()[1].split(',')
            program = [int(x) for x in program_str]

def solve(A, B, C):
    iptr = 0

    def combo(n):
        values = [9, 1, 2, 3, A, B, C]
        return values[n]

    output = []
    while iptr < len(program):
        opcode = program[iptr]
        operand = program[iptr+1]
        if opcode == 0:
            A = A // pow(2, combo(operand))
        elif opcode == 1:
            B = B ^ operand
        elif opcode == 2:
            B = combo(operand) % 8
        elif opcode == 3:
            if A != 0:
                iptr = operand - 2
        elif opcode == 4:
            B = B ^ C
        elif opcode == 5:
            output.append(combo(operand) % 8)
        elif opcode == 6:
            B = A // pow(2, combo(operand))
        elif opcode == 7:
            C = A // pow(2, combo(operand))
        iptr += 2
    
    return output

a = pow(8, 15)
n = 14

while n >= 0:
    s = solve(a, B, C)
    if s[n:] == program[n:]:
        n -= 1
        continue
    a += pow(8, n)

print("Part 1:", "".join([str(x) for x in solve(A, B, C)]))
print("Part 2:", a)
