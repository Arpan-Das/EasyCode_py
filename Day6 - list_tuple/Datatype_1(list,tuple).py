"""
Basic Datatype Examples in Python
1. Numeric Types: int, float, complex 
2. Sequence Types: list, tuple, string
3. Mapping Type: dict
4. Set Types: set, frozenset
5. Boolean Type: bool
"""

"""
1. Numeric Types
"""
# a) int: Represents integer values. +ve / -ve whole numbers.
# a = 5
# print(type(a))  # Output: <class 'int'>

# # b) float: Represents floating-point numbers (decimal values).
# b = 5.5
# print(type(b))  # Output: <class 'float'>

# # c) complex: Represents complex numbers with real and imaginary parts.
# c = 2 + 3j
# print(type(c))  # Output: <class 'complex'>

"""
2. Sequence Types
- ordered collections of items 
- it can be indexed starting from 0(zero)
- can contain duplicate elements
- similar or different data types
"""

# a) string : collections of char

# s = "My name is Avi." 
# print(type(s))
# print(s[0])
# print(s[1])
# print(s[3])
# print(s[3:7])
# print(s[14])
# print(len(s))
# print(s[-6]) # s[len(s) - 5]
# print(s[9])
# print(s[5:])

# b) list : collections of items in a particular order
# - ordered, indexed, mutable, allows duplicate elements

a = [1,2,3,4,5,4,6]
b = ["Avi", "Bivi", "Civi", "Divi"]
c = [1, "Avi", 2.5, True, 3+4j]
d = [2] * 4 # creates a list with four 2's: [2, 2, 2, 2]


print(type(a))
print(a)

print(type(b))
print(b)

print(type(c))
print(c)

print(d)
print(type(d))

print(a[3])  # Accessing element at index 3
print(a)

a.append(7)  # Adding an element to the end of the list
print(a)

a.insert(0, 8)  # Inserting an element 8 at index 0
print(a)

a[1] = 100  # Modifying element at index 1
print(a)

a.remove(2)  # Removing first occurrence of element 2
print(a)

a.pop()  # Removing and returning the last element
print(a)

a.pop(1) # Removing and returning element at index 1
print(a)

lss = list("Hello") # converting string to list
print(lss)


# list comprehension
print("List Comprehension Example:")
squares = [x**2 for x in range(1, 6) if x % 2 == 0]
print(squares)  # Output: [1, 4, 9, 16, 25]

# c) tuple : collections of items in a particular order
# - ordered, indexed, immutable, allows duplicate elements

t = (1,2,3,4,5,4,6)
ts = ("Avi", "Bivi", "Civi", "Divi")
tc = (1, "Avi", 2.5, True, 3+4j)


print(type(t))

print(ts[1])  # Accessing element at index 1
print(ts[:2])  # Slicing from index 0 to 2 (excluding 2)
print(ts[2:])  # Slicing from index 2 to end

tss = tuple("Hello") # converting string to tuple
print(tss)

tup1 = t + ts
print(tup1)

# ts[0] = "Zivi"  # This will raise an error since tuples are immutable

