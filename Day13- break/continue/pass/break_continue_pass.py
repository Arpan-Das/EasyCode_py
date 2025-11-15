'''
1. pass
✔ Definition

pass is a null statement in Python.
It does nothing, but it is used when a statement is syntactically required but you don’t want to write any code yet.

✔ When to use

As a placeholder for future code

To create empty loops, functions, or classes

To avoid syntax errors while writing incomplete code
'''

# ✔ Example
def my_function():
    pass   # I'll write the logic later

for i in range(5):
    pass   # loop does nothing for now



'''

✅ 2. break
✔ Definition

break is used to exit/terminate a loop immediately, even if the loop condition is still true.

✔ Works with

for loops

while loops
'''

# ✔ Example
for i in range(1, 10):
    if i == 5:
        break    # loop stops when i becomes 5
    print(i)

# ✔ Output
# 1
# 2
# 3
# 4


'''

✅ 3. continue
✔ Definition

continue skips the current iteration of the loop and moves to the next iteration.

✔ Useful when

You want to skip certain values or conditions but keep the loop running.
'''

# ✔ Example
for i in range(1, 6):
    if i == 3:
        continue  # skip printing 3
    print(i)

# ✔ Output
# 1
# 2
# 4
# 5