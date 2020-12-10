f = open("input.txt", "r")

voltages = [int(line.strip()) for line in f]
voltages.append(0) # add the voltage of the wall
voltages.sort()

ones = 0
threes = 1 # starts at 1 to include our adapter

for i in range(0, len(voltages)-1):
    difference = voltages[i+1] - voltages[i]
    if difference == 1:
        ones += 1
    elif difference == 2:
        continue
    elif difference == 3:
        threes += 1
    else:
        break
print(f"{ones}  {threes}")
print(ones * threes)