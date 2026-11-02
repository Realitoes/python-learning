# Q21: a running total with an if
# Before you run this, write down the EXACT output you expect.
# Then press the Run button (top right) and compare.

total = 0
for i in range(1, 6):
    if i > 2:
        total = total + i
print(total)

 # this will print 3 + 4 + 5
 # which will ultimately equal 12