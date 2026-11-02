# Q62: write it yourself
# Under the temps list, write code that:
#   1. makes a new EMPTY list called hot        ->  hot = []
#   2. goes through every temp in temps
#   3. if the temp is 30 OR MORE, adds it to hot (use .append)
#   4. after the loop, prints:  Hot days: <how many are in hot>   (use len)
#   5. then uses a SECOND loop to print each temp in hot, one per line
# Before you run it, write down the exact output you expect.

temps = [22, 31, 18, 30, 35, 27]
hot = []
for t in temps:
    if t >= 30:
        hot.append(t)

print("Hot days:", len(hot))

for h in hot:
    print(h)
 
    
