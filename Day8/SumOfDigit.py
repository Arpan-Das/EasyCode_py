"""
4. Calculate the sum of digits of a number 
e.g. 
input : 123
output: 6
reason: 1 + 2 + 3 = 6

input: 453
output: 12
reason: 4 + 5 + 3 = 12

Hint: use % and // operators
"""

# num = 1234
# rem = num %10 # 4

# num = num // 10 # 123

# ....
# num = 12
# rem = 12 % 10 = > 2
# num = 12 // 10 => 1
# rem = 1 %10 => 1

# num = 1 // 10 = > 0


num = 65
num_sum = 0
num_p = 1
while num != 0:
    rem = num %10
    num_sum += rem
    num_p *= rem
    num = num // 10

print(num_sum)
print(num_p)

