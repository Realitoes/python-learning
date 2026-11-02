# Q60: counting with an if inside the loop
# Before you run this, write down the EXACT output you expect, line by line.
# Then press the Run button (top right) and compare.

scores = [3, 5, 8, 5, 1]
count = 0
for s in scores:
    if s >= 5:
        count = count + 1
print(count)
