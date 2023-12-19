import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = f.read().split("\n\n")

    workflows = data[0].splitlines()
    workflows = [x.replace('}', '').split('{') for x in workflows]
    workflows = {x[0]:x[1].split(',') for x in workflows}

    parts = data[1].splitlines()
    parts = [{y.split('=')[0]:int(y.split('=')[1]) for y in x[1:-1].split(',')} for x in parts]

# Part 1
part1 = 0

for part in parts:    
    rule = 'in'

    while rule != 'R' and rule != 'A':
        for r in workflows[rule]:
            if ':' not in r:
                rule = r
                break

            a,d = r.split(':')
            c = a[0]
            op = a[1]
            v = int(a[2:])

            if op == '>' and part[c] > v or op == '<' and part[c] < v:
                rule = d
                break

    if rule == 'A':
        part1 += sum(part.values())

# Part 2
def ways(rule, history):
    if rule == 'A':
        table = {
            "x": [1] * 4000,
            "m": [1] * 4000,
            "a": [1] * 4000,
            "s": [1] * 4000
        }

        for h in history:
            c = h[0]
            op = h[1]
            v = int(h[2:])

            if op == '>':
                for i in range(v-1, -1, -1):
                    table[c][i] = 0
            else:
                for i in range(v-1, 4000):
                    table[c][i] = 0
        
        ans = sum(table['x']) * sum(table['m']) * sum(table['a']) * sum(table['s'])
        return ans
                    
    if rule == 'R':
        return 0
    
    ans = 0
    for r in workflows[rule]:
        if ':' not in r:
            ans += ways(r, [x for x in history])
        else:
            a,d = r.split(':')
            h = [x for x in history]
            h.append(a)
            ans += ways(d, h)

            c = a[0]
            op = a[1]
            v = int(a[2:])
            if op == '>':
                v += 1
                op = '<'
            else:
                v -= 1
                op = '>'
            history.append(c + op + str(v))
    
    return ans

part2 = ways('in', [])

print(part1, part2)
