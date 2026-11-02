# Q44: print vs return
# Before you run this, write down the EXACT output you expect, line by line.
# Then press the Run button (top right) and compare.

def show(n):
    print(n + 1)

def give(n):
    return n + 1

x = show(3)
y = give(3)
print(y)
print(x)
