import sys
from collections import Counter

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
hands1 = []
hands2 = []

with open(file) as f:
    for line in f:
        line = line.strip().split()
        line.append(0)
        hands1.append(line)
        hands2.append(line)

# Part 1
for idx, (hand, bet, t) in enumerate(hands1):
    count = Counter(hand).most_common()
    if count[0][1] == 5:
        t = 6
    elif count[0][1] == 4:
        t = 5
    elif count[0][1] == 3 and count[1][1] == 2:
        t = 4
    elif count[0][1] == 3:
        t = 3
    elif count[0][1] == 2 and count[1][1] == 2:
        t = 2
    elif count[0][1] == 2:
        t = 1
    value = int(hand.replace("A", "E").replace("K", "D").replace("Q", "C").replace("J", "B").replace("T", "A"), 16)
    hands1[idx] = (value, int(bet), t)


hands1.sort()
hands1.sort(key=lambda x:x[2])

part1 = sum([bet * (idx + 1) for idx, (_, bet, _) in enumerate(hands1)])

# Part 2
for idx, (hand, bet, t) in enumerate(hands2):
    num_jokers = len([x for x in hand if x == 'J'])

    count = Counter(hand.replace("J", "")).most_common()
    if num_jokers == 5 or count[0][1] + num_jokers == 5:
        t = 6
    elif count[0][1] + num_jokers == 4:
        t = 5
    elif count[0][1] + num_jokers == 3 and count[1][1] == 2:
        t = 4
    elif count[0][1] + num_jokers == 3:
        t = 3
    elif count[0][1] + num_jokers == 2 and count[1][1] == 2:
        t = 2
    elif count[0][1] + num_jokers == 2:
        t = 1
    value = int(hand.replace("A", "E").replace("K", "D").replace("Q", "C").replace("J", "1").replace("T", "A"), 16)
    hands2[idx] = (value, int(bet), t)


hands2.sort()
hands2.sort(key=lambda x:x[2])

part2 = sum([bet * (idx + 1) for idx, (_, bet, _) in enumerate(hands2)])

print(part1, part2)
