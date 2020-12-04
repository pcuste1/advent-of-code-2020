import re

valid = 0
for line in open("input.txt", "r"):
    rng,let,pas = line.split(' ')

    low,up = rng.split('-')
    count = len(pas.split(let[0])) - 1
    if count >= int(low) and count <= int(up):
        valid += 1

print(valid)