"""
After some careful analysis, you believe that exactly one instruction is corrupted.

Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to be a jmp. (No acc instructions were harmed in the corruption of this boot code.)

The program is supposed to terminate by attempting to execute an instruction immediately after the last instruction in the file. By changing exactly one jmp or nop, you can repair the boot code and make it terminate correctly.

For example, consider the same program from above:

nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
If you change the first instruction from nop +0 to jmp +0, it would create a single-instruction infinite loop, never leaving that instruction. If you change almost any of the jmp instructions, the program will still eventually find another jmp instruction and loop forever.

However, if you change the second-to-last instruction (from jmp -4 to nop -4), the program terminates! The instructions are visited in this order:

nop +0  | 1
acc +1  | 2
jmp +4  | 3
acc +3  |
jmp -3  |
acc -99 |
acc +1  | 4
nop -4  | 5
acc +6  | 6
After the last instruction (acc +6), the program terminates by attempting to run the instruction below the last instruction in the file. With this change, after the program terminates, the accumulator contains the value 8 (acc +1, acc +1, acc +6).

Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). What is the value of the accumulator after the program terminates?

Your puzzle answer was 1000.
"""

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