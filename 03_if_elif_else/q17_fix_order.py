# Q17: fix the bug
# This is the code from Q16. A score of 90 gets a "C", which is wrong.
# Change the code below so that:
#   85 or more  -> A
#   70 to 84    -> B
#   50 to 69    -> C
#   below 50    -> fail
# When you're done, press Run. With score = 90 it should print A.

score = 90
if score >= 85:
    print("A")
elif score >= 70:
    print("B")
elif score >= 50:
    print("C")
else:
    print("fail")
