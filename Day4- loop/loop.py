"""
Loops in Python are used to repeat actions efficiently.
The main types are 
a) For loops (counting through items) and 

Syntax
for i in range(starting, ending, increment):
    statement

Note: starting <= 1 < ending
By Default increment is 1
By Default if one argument is assed it will set starting index a 0 

b) While loops (based on conditions).

Syntax:
while condition:
    statement

c) do-while loop 
"""

# For_loop
# range(starting, ending(not included), increment)

# for i in range(1, 6):
#     print(i)

# for i in range(1, 11, 3):
#     print(i)

# for i in range(6):
#     print(i)



# while loop

i = 1

# while i <= 5:
#     print(i)
#     i += 1   # i = i + 1

# while i < 6:
#     print(i)
#     i += 2


"""
initial value i = 1

iteration   i  conditon(i <= 5)  print(i)  i += 1
1st         1       True            1       2
2nd         2       True            2       3
3rd         3       True            3       4
4th         4       True            4       5
5th         5       True            5       6
6th         6       False 
loop end 
"""




