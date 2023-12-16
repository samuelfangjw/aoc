import sys
import re

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = []

with open(file) as f:
    for line in f:
        line = line.strip()
        data.append(line)

part1, part2 = 0, 0

words = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

regex = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'

for line in data:
    # part 1
    nums = [x for x in line if x.isdigit()]
    part1 += int(nums[0] + nums[-1])

    # part 2
    nums = re.findall(regex, line)
    nums = [words[num] if num in words else num for num in nums]
    part2 += int(nums[0] + nums[-1])

print(part1, part2)
