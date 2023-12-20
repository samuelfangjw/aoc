import sys
import math
from collections import deque

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
modules, states = {}, {}
conjunction = set()

with open(file) as f:
    for line in f:
        line = line.strip()
        a,b = line.split(" -> ")
        t = "none"
        if "%" in a or "&" in a:
            t = a[0]
            a = a[1:]
        modules[a] = {
            "t": t,
            "d": b.split(', ')
        }
        states[a] = False
        if t == '&':
            conjunction.add(a)
            modules[a]['inputs'] = {}

for m, ds in modules.items():
    for d in ds['d']:
        if d in conjunction:
            modules[d]['inputs'][m] = False

pulses = {
    "low": 0,
    "high": 0
}

conjuction_cycles = {}

for a,b in modules.items():
    if 'rx' in b['d']:
        target = a
        break

to_check = list(modules[a]['inputs'].keys())

i = 0
while len(conjuction_cycles) < 4:
    q = deque()
    q.append(('broadcaster', "low", ""))

    if i == 1000:
        part1 = pulses['high'] * pulses['low']

    while q:
        m, p, prev = q.popleft()

        pulses[p] += 1

        if m not in modules:
            continue

        send_pulse = True

        if modules[m]['t'] == '%':
            if p == 'low':
                states[m] = not states[m]
                if states[m]:
                    p = 'high'
                else:
                    p = 'low'
            else:
                send_pulse = False
        elif modules[m]['t'] == '&':
            if p == 'low':
                modules[m]['inputs'][prev] = False
            else:
                modules[m]['inputs'][prev] = True

            flag = True
            for x in modules[m]['inputs'].values():
                flag = flag and x

            if flag:
                p = 'low'
            else:
                p = 'high'
            
                if m in to_check:
                    conjuction_cycles[m] = i + 1
        
        if send_pulse:
            for d in modules[m]['d']:
                q.append((d, p, m))
    i += 1

part2 = math.lcm(*conjuction_cycles.values())

print(part1, part2)
