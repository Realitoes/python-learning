# Q42: a function with if inside
# Before you run this, write down the EXACT output you expect, line by line.
# Then press the Run button (top right) and compare.

def grade(score):
    if score >= 85:
        return "A"
    elif score >= 70:
        return "B"
    else:
        return "C"

print(grade(90))
print(grade(70))
print(grade(69))
