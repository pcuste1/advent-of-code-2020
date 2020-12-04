import re

valid = 0
for line in open("input.txt", "r"):
    rng,let,pas = line.split(' ')
    let = let[0]
    x,y = rng.split('-')

    if ( pas[int(x)-1] == let ) ^ ( pas[int(y)-1] == let ):
        valid += 1

print(valid)