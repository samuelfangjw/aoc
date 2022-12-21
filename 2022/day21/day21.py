import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = f.read().strip()

monkeys = {}
for line in data.splitlines():
    monkey, other = line.split(": ")
    monkeys[monkey] = other


def solve(m, part):
    # solve symbolically
    x = monkeys[m]

    if len(x.split()) > 1:
        a, op, b = x.split()
        a = solve(a, part)
        b = solve(b, part)

        if part == 2 and m == 'root':
            return a, b
        elif op == '+':
            if 'x' not in a and 'x' not in b:
                return str(int(a) + int(b))
            else:
                return '(' + a + ' + ' + b + ')'
        elif op == '-':
            if 'x' not in a and 'x' not in b:
                return str(int(a) - int(b))
            else:
                return '(' + a + ' - ' + b + ')'
        elif op == '*':
            if 'x' not in a and 'x' not in b:
                return str(int(a) * int(b))
            else:
                return '(' + a + ' * ' + b + ')'
        else:
            if 'x' not in a and 'x' not in b:
                return str(int(a) // int(b))
            else:
                return '(' + a + ' // ' + b + ')'
    else:
        return x


part1 = eval(solve('root', 1))
print(part1)

monkeys["humn"] = '(x)'
a, b = solve('root', 2)

if 'x' in a:
    eqn = a
    curr = int(b)
else:
    eqn = b
    curr = int(a)

# solve for x
while eqn[0] == '(':
    eqn = eqn[1:-1]
    if eqn == 'x':
        break

    if eqn[0] != '(':
        idx = 0
        while eqn[idx] != '(':
            idx += 1
        n, op = eqn[0:idx].strip().split()
        eqn = eqn[idx:]
        if op == '+':
            curr -= int(n)
        elif op == '-':
            curr = int(n) - curr
        elif op == '*':
            curr = curr // int(n)
        else:
            curr = int(n) // curr
    else:
        idx = len(eqn) - 1
        while eqn[idx] != ')':
            idx -= 1
        op, n = eqn[idx+1:].strip().split()
        eqn = eqn[0:idx+1]
        if op == '+':
            curr -= int(n)
        elif op == '-':
            curr += int(n)
        elif op == '*':
            curr = curr // int(n)
        else:
            curr *= int(n)

part2 = curr
print(part2)
