# Q61: write it yourself
# Under the list, write code that:
#   1. goes through every age in the list
#   2. counts how many people are 18 OR OLDER (adults)
#   3. after the loop, prints:  Adults: <the count>
# Before you run it, write down the exact output you expect.

ages = [12, 18, 25, 17, 40, 9]
count = 0
for a in ages:
    if a >= 18:
        count = count + 1

print("Adults:", count)
    