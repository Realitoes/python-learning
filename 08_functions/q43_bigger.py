# Q43: write it yourself
# Write a function called bigger that takes TWO numbers, a and b,
# and RETURNS whichever one is bigger.
# Then add these three lines below it, exactly:
#     print(bigger(3, 7))
#     print(bigger(10, 2))
#     print(bigger(5, 5))
# Before you run it, write down the EXACT output you expect.
# Write your code below this line.

def bigger(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return a

print(bigger(3, 7))
print(bigger(10, 2))
print(bigger(5, 5))
