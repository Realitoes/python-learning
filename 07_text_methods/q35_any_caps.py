# Q35: accept any capitals
# Change the code so that Banana, BANANA and banana ALL print "Welcome in".
# Run it three times to test each one.

password = input("Password: ").lower()
if password == "banana":
    print("Welcome in")
else:
    print("Wrong password")
