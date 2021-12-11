import sys
import itertools
import re
from statistics import mean, median
from collections import defaultdict, deque

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = []

with open(file) as f:
    for line in f:
        line = line.strip()
        data.append([int(x) for x in line])