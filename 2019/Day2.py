f = open("input2.txt")
s = f.readline()
tokens = s.split(',')

def run_program(noun, verb):
    global mem
    mem = list(map(int, tokens))
    mem[1] = noun
    mem[2] = verb

    for i in range(0, len(mem), 4):
        opcode = mem[i]
        if opcode == 99:
            break
        
        a, b, c = mem[i+1], mem[i+2], mem[i+3]

        if opcode == 1:
            mem[c] = mem[a] + mem[b]
        else:
            mem[c] = mem[a] * mem[b]

# Part 1
run_program(12, 2)
print("Part 1: " + str(mem[0]))

#Part 2
for i in range(100):
    for j in range(100):
        run_program(i, j)
        if mem[0] == 19690720:
            print("Part 2: " + str(100 * i + j))
            break