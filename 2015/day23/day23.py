import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
instructions = []

with open(file) as f:
    for line in f:
        instructions.append(line.strip())

def run(a,b):
    i = 0
    while 0 <= i < len(instructions):
        inst, body = instructions[i].split(" ", 1)
        if inst == 'hlf':
            if body == 'a':
                a = a // 2
            else:
                b = b // 2
        elif inst == 'tpl':
            if body == 'a':
                a *= 3
            else:
                b *= 3
        elif inst == 'inc':
            if body == 'a':
                a += 1
            else:
                b += 1
        elif inst == 'jmp':
            i += int(body)
            continue
        elif inst == 'jie':
            r, offset = body.split(", ")
            if r == 'a' and a % 2 == 0:
                i += int(offset)
                continue
            elif r == 'b' and b % 2 == 0:
                i += int(offset)
                continue
        elif inst == 'jio':
            r, offset = body.split(", ")
            if r == 'a' and a == 1:
                i += int(offset)
                continue
            elif r == 'b' and b == 1:
                i += int(offset)
                continue
        i += 1
    print(b)

run(0,0)
run(1,0)
