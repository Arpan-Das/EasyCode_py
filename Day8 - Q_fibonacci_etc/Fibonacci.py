"""
5.Print Fibonacci series up to N terms

e.g. sum of its previous 2 numbers 
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ....
"""

n = 10

num1 = 0
num2 = 1

print(num1)
print(num2)

while n >= 2:
    num3 = num1 + num2
    print(num3)
    num1 = num2
    num2 = num3
    n -= 1
