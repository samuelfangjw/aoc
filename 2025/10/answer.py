from collections import deque
import sys

import z3

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file, "r") as f:
    lines = [line.strip() for line in f.readlines()]

machines = []
for line in lines:
    raw = line.split()
    num_machines = len(raw[0]) - 2

    lights = 0
    for i, ch in enumerate(reversed(raw[0][1:-1])):
        if ch == "#":
            lights |= 1 << i

    buttons = [tuple(map(int, t.strip("()").split(","))) for t in raw[1:-1]]
    buttons_masks = []
    for btn in buttons:
        mask = 0
        for b in btn:
            mask |= 1 << (num_machines - b - 1)
        buttons_masks.append(mask)

    joltages = tuple(map(int, raw[-1].strip("{}").split(",")))

    machines.append((lights, buttons, buttons_masks, joltages))


def configure_indicators(lights, buttons_masks):
    q = deque([(0, 0)])  # (cost, state)
    visited = set()

    while q:
        cost, state = q.popleft()
        if state in visited:
            continue
        visited.add(state)

        if state == lights:
            return cost

        for button in buttons_masks:
            new_state = state ^ button
            new_cost = cost + 1
            q.append((new_cost, new_state))


def configure_joltage(buttons, joltages):
    m = z3.Optimize()
    n_buttons = len(buttons)
    n_j = len(joltages)

    # Decision vars: presses per button (non-negative integers)
    x = [z3.Int(f"x_{i}") for i in range(n_buttons)]
    for xi in x:
        m.add(xi >= 0)

    # Constraints: for each joltage dimension j, sum of contributions == target
    for j in range(n_j):
        m.add(
            z3.Sum(x[i] * (1 if j in buttons[i] else 0) for i in range(n_buttons))
            == joltages[j]
        )

    # Objective: minimize total presses
    total_presses = z3.Sum(x)
    m.minimize(total_presses)

    if m.check() != z3.sat:
        return float("inf")

    model = m.model()
    return sum(model[xi].as_long() for xi in x)


part1, part2 = 0, 0

for lights, buttons, buttons_mask, joltages in machines:
    part1 += configure_indicators(lights, buttons_mask)
    part2 += configure_joltage(buttons, joltages)

print("Part 1:", part1)
print("Part 2:", part2)
