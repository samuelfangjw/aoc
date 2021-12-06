import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    input = []
    for line in f:
        line = line.strip()
        input.append(line)

code, decode, encode = 0, 0, 0

for x in input:
    code += len(x)
    decode += len(x.decode('string_escape')) - 2
    encode += len(x.encode('unicode-escape').replace(b'"', b'\\"')) + 2

part1 = code - decode
part2 = encode - code
print(part1)
print(part2)
