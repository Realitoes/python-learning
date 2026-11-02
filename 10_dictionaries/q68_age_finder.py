# Q68: write it yourself - age finder
# Under the ages dictionary, write code that:
#   1. asks the user to type a name (use input)
#   2. if that name is in ages, prints their age, e.g.  Alex is 17
#   3. otherwise prints:  not found
# Before you run it, write down the exact output you expect
# if you type  Mia , and if you type  Bob .

ages = {"sam": 15, "alex": 17, "mia": 12}

name = input("Who are you looking for? ").lower()
if "sam" in ages:
    print("Sam is", ages[name])
elif "alex" in ages:
    print("Alex is", ages[name])
elif "mia" in ages:
    print("Mia is", ages[name])
else:
    print("Unknown person")

# you may continue adding names with
# elif name == "Intended Name":
#   print("name", "is", ages[name])

# I want to figure out how to make the input turn into lowercase
# so that it isn't case sensitive

#update, found out how