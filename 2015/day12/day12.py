import sys
import json

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    input = []
    for line in f:
        line = line.strip()
        input = line

data = json.loads(input)

def count(data, ignore):
    if isinstance(data, str):
        return 0
    elif isinstance(data, int):
        return data
    elif isinstance(data, list):
        return sum(count(val, ignore) for val in data)
    elif ignore and "red" in data.values():
        return 0
    else:
        return sum(count(val, ignore) for val in data.values())

print(count(data, False))
print(count(data, True))