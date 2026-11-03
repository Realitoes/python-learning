# Q86: moving the body - add a new head, remove the tail
# .append(...) adds to the END of a list (you used it in Q59).
# .pop(0) removes the item at position 0 (the FRONT of the list).
# Here the END of the list is the head, and the FRONT is the tail.
# Predict the EXACT output (2 lines) before you run it.

body = [[100, 40], [120, 40], [140, 40]]

body.append([160, 40])
body.pop(0)

print(body)
print(len(body))
