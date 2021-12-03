with open("input.txt") as f:
    input1 = f.readlines()
    input2 = input1[:]

# Part 1
rows = len(input1)
gamma = ""
epsilon = ""

for i in range(len(input1[0]) - 1):
    num_ones = 0
    for line in input1:
        num_ones = num_ones + int(line[i])
    num_zeros = rows - num_ones

    if num_ones >= num_zeros:
        gamma = gamma + "1"
        epsilon = epsilon + "0"
    else:
        gamma = gamma + "0"
        epsilon = epsilon + "1"
    
part1 = int(gamma, 2) * int(epsilon, 2)

# Part 2
oxygen = input2[:]
co2 = input2[:]

# Calculate oxygen generator rating
for i in range(len(oxygen[0]) - 1):
    if len(oxygen) == 1:
        break
    num_ones = 0
    for line in oxygen:
        num_ones = num_ones + int(line[i])
    num_zeros = len(oxygen) - num_ones
    if num_ones >= num_zeros:
        oxygen = list(filter(lambda x: x[i] == "1", oxygen))
    else:
        oxygen = list(filter(lambda x: x[i] == "0", oxygen))

# Calculate CO2 scrubber rating
for i in range(len(co2[0]) - 1):
    if len(co2) == 1:
        break
    num_ones = 0
    for line in co2:
        num_ones = num_ones + int(line[i])
    num_zeros = len(co2) - num_ones
    if num_ones >= num_zeros:
        co2 = list(filter(lambda x: x[i] == "0", co2))
    else:
        co2 = list(filter(lambda x: x[i] == "1", co2))

part2 = int(oxygen[0], 2) * int(co2[0], 2)

print(part1)
print(part2)
