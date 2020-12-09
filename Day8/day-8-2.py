import copy

f = open("input.txt", 'r')
instruction_set = []
for line in f:
    line = line.strip().split(' ')
    instruction_set.append((line[0], int(line[1])))

def test_instructions(instruction_set):
    count = 0
    pos = 0
    prev = []
    while pos < len(instruction_set):
        if pos in prev:
            return False
        prev.append(pos)

        inst, val = instruction_set[pos]    
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
    return True

for i in range(0, len(instruction_set)):
    test_set = copy.deepcopy(instruction_set)
    curr, val = test_set[i]
    if curr == "jmp":
        test_set[i] = ("nop", val)
    elif curr == "nop":
        test_set[i] = ("jmp", val)

    if(test_instructions(test_set)):
        break