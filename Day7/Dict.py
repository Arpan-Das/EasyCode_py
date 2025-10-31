"""
Dictionary
1. stores data in key:value pairs
2. unordered, changeable, indexed
3. keys are unique
"""

d1 = {"Name": "John", "Age": 30, "City": "New York"}
# print(d1)
# print(type(d1))

# Accessing values
# print(d1["Name"]) # John
# print(d1.get("Age")) # 30

# Adding items
# d1["Occupation"] = "Engineer"
# print(d1)

# Modifying items
# d1["Age"] = 100
# print(d1)

# Removing items
# print("before ",d1)
# print(d1.pop("City")) # removes item with key "City"
# print("After ", d1)

# del d1["Age"] # removes item with key "Age"
# print("After", d1)

# key, val = d1.popitem() # removes last inserted item
# print("Popped item:", key, val)
# print("After popitem ", d1)

# d1.clear() # removes all items
# print("After clear ", d1)

# Looping through dictionary
# print(d1)
# print("using keys")
# print("keys are:", d1.keys())
# for key in d1:  
#     print(key, ":", d1[key])

# print("\n using values")
# print("values are:", d1.values())
# for value in d1.values():
#     print(value)

# # Iterate through both keys and values
# print("\n using items()")
# for key, value in d1.items():
#     print(key, ":", value)


print("\nNested Dictionary")
d2 = {
    "Name": "Alice",
    "Age": 25,
    "City": "Los Angeles",
    "Address": {
        "Village": "Muradpur",
        "City": "Los Angeles",
        "State": "CA",
        "Pin": "90001",
    }
}
# print(d2)
print("city :", d2["Address"]["City"])  # Accessing nested dictionary value