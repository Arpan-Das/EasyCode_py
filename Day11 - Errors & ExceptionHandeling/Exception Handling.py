'''
Introduction, handling exceptions using try-except-finally blocks.


# Handling exceptions
An exception is an error that occurs during program execution (run-time), which interrupts the normal flow of the program.

Example of Exceptions:

ZeroDivisionError → when dividing a number by zero
ValueError → when an invalid value is given to a function
IndexError → when accessing an invalid index in a list
FileNotFoundError → when trying to open a non-existing file

'''

# l = [0, 1, 2, 3, 4]
# print(l[5]) # IndexError: list index out of range

# print("Start of program")
# a = 10
# b = 0
# print(a / b)  # Error: Division by zero
# print("End of program")


'''
2. What is Exception Handling?
Exception Handling is a way to handle errors gracefully without crashing the program.

Python provides special keywords for this:
try
except
finally
(also else and raise – optional advanced topics)

try:
    # Code that might cause an error
except:
    # Code to handle the error
finall:
    # Code to do finally 
'''

# print("Start of program")
# try:
#     a = 10
#     b = 0
#     print(a / b)
# except:
#     print("An error occurred!")
# print("End of program")



'''
# Handling Specific Exceptions
# '''

# try:
#     num = int(input("Enter a number :"))
#     print(10 / num)
# except ValueError:
#     print("Please enter a valid number.")
# except ZeroDivisionError: 
#     print('Cannot divide by zero.')

'''
# finally Block
The finally block always executes — whether an exception occurs or not.
It is often used for clean-up tasks (like closing a file or releasing resources).
# '''


print("Start of program")
try:
    num = int(input("Enter a number : "))
    print(10 / num)
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError: 
    print('Cannot divide by zero.')
finally:
    print("this block alwasy run.")
print("End of program")