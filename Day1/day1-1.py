f = open("nums.txt", "r")
nums = [int(line) for line in f]

for x in range(0, len(nums)):
    for y in range(x, len(nums)):
            if nums[x] + nums[y] == 2020:
                print(nums[x]*nums[y])