from functools import cache
import sys
import itertools
import re
import math
from copy import copy, deepcopy
from statistics import mean, median
from collections import Counter, defaultdict, deque

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(file) as f:
    data = []
    for line in f:
        line = line.strip()
        # line = line.strip().split()
        # res = re.search('abc-(\d+)-(.+)-', line)
        # data.append(res.groups())
        data.append(line)
        # data.append([int(x) for x in line])

print(data)
