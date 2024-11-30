import sys
import itertools
import re
from collections import deque

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
starting_items = []

with open(file) as f:
    for idx, line in enumerate(f):
        line = line.strip()

        generators = [(ele + "G", idx + 1) for ele, _ in re.findall(r"(\w+)(?=\s(generator))", line)]
        microchips = [(ele + "M", idx + 1) for ele, _ in re.findall(r"(\w+)(?=(-compatible microchip))", line)]

        starting_items.extend(generators + microchips)

state = (tuple(starting_items), 1, 0)

def reduced_state(items, mapping, elevator):
    state = [elevator]
    for i in range(1, 5):
        f_items = [item for item, floor in items if floor == i]
        generators = set()
        for item in f_items:
            if item.endswith("G"):
                generators.add(mapping[item])
        
        has_pairs = False
        has_unpaired = False
        for item in f_items:
            if item.endswith("M"):
                if mapping[item] in generators:
                    f_items.remove(item)
                    has_pairs = True
                    state.append(("P", i))
                else:
                    has_unpaired = True
                    state.append(("I", i))
        if has_pairs and has_unpaired:
            return None # invalid state
        for item in generators:
            state.append(("G", i))
    return tuple(state)


def run_queue(initialState):
    mapping = {item: item[:-1] for item, _ in initialState[0]}
    rs = reduced_state(initialState[0], mapping, 1)
    initialState.append(rs)
    queue = deque([initialState])
    seen = set()

    while queue:
        items, elevator, steps, r_state = queue.popleft()
        
        if r_state in seen:
            continue

        seen.add(r_state)

        if elevator == 4 and all(floor == 4 for _, floor in items):
            return steps

        items_on_floor = {l: [item for item, floor in items if floor == l] + [None] for l in range(1,5)}
        
        for item1, item2 in itertools.combinations(items_on_floor[elevator], 2):
            min_floor = 1
            if len(items_on_floor[1]) == 1:
                min_floor += 1
                if len(items_on_floor[2]) == 1:
                    min_floor += 1

            if elevator < 4:
                new_items = [(item, floor + 1) if item == item1 or item == item2 else (item, floor) for item, floor in list(items)]

                r_state = reduced_state(new_items, mapping, elevator + 1)
                if r_state:
                    queue.append((tuple(new_items), elevator + 1, steps + 1, r_state))
            
            if elevator > 1 and elevator >= min_floor:
                new_items = [(item, floor - 1) if item == item1 or item == item2 else (item, floor) for item, floor in list(items)]

                r_state = reduced_state(new_items, mapping, elevator - 1)
                if r_state:
                    queue.append((tuple(new_items), elevator - 1, steps + 1, r_state))

part_1_data = [tuple(starting_items), 1, 0]
part_2_data = [tuple(starting_items + [("eleriumG", 1), ("eleriumM", 1), ("dilithiumG", 1), ("dilithiumM", 1)]), 1, 0]

print("Part 1:", run_queue(part_1_data))
print("Part 2:", run_queue(part_2_data))
