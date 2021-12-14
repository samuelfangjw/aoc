import sys
from collections import Counter

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
insertions = {}

with open(file) as f:
    data = f.readlines()
    text = data[0].strip()
    for line in data[2:]:
        line = line.strip().split(" -> ")
        a,b = line
        insertions[a] = b

def solve(iterations):
    count = Counter(text)
    pairs_start = Counter(["".join(x) for x in zip(text[:-1], text[1:]) if "".join(x) in insertions])

    for _ in range(iterations):
        pairs_end = Counter()
        for x in pairs_start.keys():
            new_char = insertions[x]
            inc = pairs_start[x]
            count[new_char] += inc
            pairs_end[x[0] + new_char] += inc
            pairs_end[new_char + x[1]] += inc
        pairs_start = pairs_end

    print(count.most_common()[0][1] - count.most_common()[-1][1])

solve(10)
solve(40)
