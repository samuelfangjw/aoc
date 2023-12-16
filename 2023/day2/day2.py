import sys

file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
games = []

with open(file) as f:
    for line in f:
        line = line.strip().split(": ")[1].split("; ")
        line = [x.split(", ") for x in line]
        games.append(line)

# part 1: only 12 red cubes, 13 green cubes, and 14 blue cubes
limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}

part1, part2 = 0, 0

for idx, game in enumerate(games):
    red, green, blue = 0, 0, 0
    possible = True

    minimum = {
        "red": 0,
        "blue": 0,
        "green": 0
    }

    for xs in game:
        for x in xs:
            num, color = x.split()

            if int(num) > limits[color]:
                possible = False

            minimum[color] = max(int(num), minimum[color])

    if possible:
        part1 += idx + 1

    part2 += minimum["blue"] * minimum["green"] * minimum["red"]

print(part1, part2)
