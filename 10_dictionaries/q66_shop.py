# Q66: write it yourself
# Under the prices dictionary, write code that:
#   1. goes through every item in prices
#   2. prints the item and its price on one line, e.g.  apple 2
#   3. adds each price to a running total
#   4. after the loop, prints:  Total: <the total>
# Before you run it, write down the exact output you expect, line by line.

prices = {"apple": 2, "bread": 4, "milk": 3}
total = 0
for item in prices:
    print(item, prices[item])
    total = total + prices[item]

print("Total Price:", total)

