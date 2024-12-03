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
        # pattern = re.compile(r'mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))')
        # res = re.findall(pattern, line)
        # data.extend(res)
        data.append(line)
        # data.append([int(x) for x in line])

print(data)
