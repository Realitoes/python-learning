# Q18: write it from scratch
# Write code that looks at temp and prints:
#   30 or more  -> hot
#   20 to 29    -> warm
#   10 to 19    -> cool
#   below 10    -> cold
# Start with temp = 25. When it works, try temp = 30, 20 and 10 too.

temp = -13
if temp >= 30:
    print("hot")
elif temp >= 20:
    print("warm")
elif temp >= 10:
    print("cool")
elif temp < 10:
    print("cold")