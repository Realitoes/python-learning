# Q70: a loop that runs until we switch it off
# Before you run this, write down the EXACT output you expect, line by line.
# Then press the Run button (top right) and compare.

running = True
lives = 3
while running:
    print("lives:", lives)
    lives = lives - 1
    if lives == 0:
        running = False
print("game over")
