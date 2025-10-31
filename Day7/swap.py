"""
swap between two variables
"""

var1 = 10
var2 = 20

""" objective to swap both the values  """

print("Before swapping:")
print("var1 =", var1)
print("var2 =", var2)

temp = var1
var1 = var2
var2 = temp

print("After swapping:")
print("var1 =", var1)       
print("var2 =", var2)


""" swap without using third variable  """

print("\nSwap without using third variable:")
var1 = 10
var2 = 20

print("Before swapping:")
print("var1 =", var1)   
print("var2 =", var2)

var1 = var1 + var2 # var1 now becomes 30 note we have var2 = 20 
var2 = var1 - var2 # var2 becomes 10 note var1 = 30
var1 = var1 - var2 # var1 becomes 20 note var2 = 10

print("After swapping:")
print("var1 =", var1)   
print("var2 =", var2)
