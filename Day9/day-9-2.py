"""
The final step in breaking the XMAS encryption relies on the invalid number you just found: you must find a contiguous set of at least two numbers in your list which sum to the invalid number from step 1.

Again consider the above example:

35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
In this list, adding up all of the numbers from 15 through 40 produces the invalid number from step 1, 127. (Of course, the contiguous set of numbers in your actual list might be much longer.)

To find the encryption weakness, add together the smallest and largest number in this contiguous range; in this example, these are 15 and 47, producing 62.

What is the encryption weakness in your XMAS-encrypted list of numbers?

Your puzzle answer was 3535124.
"""

def find_contiguous(target, values):
    curr = []
    for x in values:
        # make a rolling shutter and pop from beginning when sum gets too large
        curr.append(x)
        while(sum(curr) > target):
            curr.pop(0)
        if sum(curr) == target:
            return curr

def contains_sum(target, values):
    for x in range(0, 25):
        for y in range(x+1, 25):
            if values[x] + values[y] == target:
                return True
    return False

f = open("input.txt", "r")

lines = [ int(line.strip()) for line in f]

for i in range(25, len(lines)):
    if not contains_sum(lines[i], lines[i-25:i]):
        contiguous = find_contiguous(lines[i], lines[:i])
        contiguous.sort()
        encryption_weakness = contiguous[0] + contiguous[-1]
        print(encryption_weakness)
        break