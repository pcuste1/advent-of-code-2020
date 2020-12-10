"""
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

Your puzzle answer was 76110336.
"""

f = open("nums.txt", "r")
nums = [int(line) for line in f]

for x in range(0, len(nums)):
    for y in range(x, len(nums)):
        for i in range(y, len(nums)):
            if nums[x] + nums[y] + nums[i] == 2020:
                print(nums[x]*nums[y]*nums[i])