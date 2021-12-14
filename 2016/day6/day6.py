import sys
from collections import Counter

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = []

with open(file) as f:
    data = f.readlines()
    data = [[x[i] for x in data] for i in range(len(data[0])-1)]

msg = "".join([Counter(x).most_common(1)[0][0] for x in data])
print(msg)

msg = "".join([Counter(x).most_common()[-1][0] for x in data])
print(msg)
