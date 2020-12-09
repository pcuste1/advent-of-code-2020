f = open("input.txt", 'r')
instruction_set = []
for line in f:
    line = line.strip().split(' ')
    instruction_set.append((line[0], int(line[1])))

count = 0
pos = 0
prev = []
while pos < len(instruction_set):
    if pos in prev:
        break
    prev.append(pos)

    inst, val = instruction_set[pos]    
    print(f"{inst} {val}")
    if inst == "acc":
        count += val
        pos += 1
    elif inst == "jmp":
        pos += val
    elif inst == "nop":
        pos += 1
    else:
        pos += 1

print(count)
