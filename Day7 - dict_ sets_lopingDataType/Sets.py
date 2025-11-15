"""
Sets
1. unordered collection of multiple items having different datatypes
2. unindexed, 
3. unchangeable
4. no duplicate values

"""

set1 = {1, 2, 3, 4}
set2 = {"Apple", "Banana", "Cherry"}
set3 = {1, "Hello", 3.14, False}
set4 = set("Helloa") # from string
set5 = set()

# print(set1)
# print(type(set1)) #<class 'set'>
# print(set2) 
# print(set3) 
# print(set4) # {'e', 'H', 'l', 'o'}

# Adding items
# set5.add(10)
# set5.add(11)
# set5.add(20)
# set5.add(10) # duplicate value, will be ignored
# print("Set5 after adding items:", set5)

# # Removing items
# set5.remove(11) # raises error if item not found
# print("Set5 after removing 11:", set5)

# # set5.remove(30) # raises error if item not found
# # print("Set5 after removing 30:", set5)

# set5.discard(30) # does not raise error if item not found
# print("Set5 after discarding 30:", set5)

# set5.pop() # removes and returns an arbitrary item
# print("Set5 after pop():", set5)

# set5.clear() # removes all items
# print("Set5 after clear():", set5)

# Looping through a set
set6 = {1, 2, 3, 4, 5}
print("Looping through set6:") 
for item in set6:
    print(item)