'''
Errors: Syntax errors, logical errors, and run-time errors


What is Error ?
An error is a problem in a program that stops it from running correctly.

Errors are mainly divided into three types: 
1) Syntax Error 
2) Lgical Error
3) Run-Time Error

'''


'''
#1) Syntax Error: A syntax error occurs when the rules (grammar) of the Python language are broken.
e.g. 
'''
# print("hello")

# print("hello" #SyntaxError: '(' was never closed

# def test1() # SyntaxError: expected ':'
#     print("statement1")

# prin("hasdfasd") #NameError: name 'prin' is not defined. Did you mean: 'print'?


'''
# 2. Logical Error : A logical error means the program runs
# successfully, but the output is wrong because the logic or 
# formula used is incorrect.
'''


# Calculate the average of two numbers
a = 10
b = 20

# e.g of logical error
average = a + b / 2  #Division happens before addition (operator precedence), so parentheses are needed. 
# print("Average is:", average)

# correct version
average = (a + b) / 2
# print("Average is:", average)


'''
# 3. Run-Time Error : A run-time error (also called an exception) occurs while the program is running — usually due to invalid operations such as dividing by zero, opening a missing file, or using an invalid index.
'''


a = 10
b = 0
print(a / b) #ZeroDivisionError: division by zero