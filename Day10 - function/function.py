# print(2*4)
# print(6*5)
# print(10*45)

# print("making a pizza with mushrooms")
# print("adding cheese")
# print("adding onion")
# print("baking your pizza")
# print("here's your mushrooms pizza!")

# print("making a pizza with chicken")
# print("adding cheese")
# print("adding onion")
# print("baking your pizza")
# print("here's your chicken pizza")

# print("making a pizza with xyz")
# print("adding cheese")
# print("adding onion")
# print("baking your pizza")
# print("here's your xyz pizza")

# print("making a pizza with xyz1")
# print("adding cheese")
# print("baking your pizza")
# print("here's your xyz1 pizza")


'''
Fuction:
--------
Functions are a block of statements that does a specific task. The idea is to put some commonly
or repeatedly done task together and make a function so that instead of writing the same code again and
again for different inputs, we can do the function calls to reuse code contained in it over and over 
again.

input -> |function| -> output
2     -> [square]   -> 4
4     -> [square]   -> 16

2     -> [cube]   -> 8


syntex:

def function_name(input_parameters):
    statement1
    statement2

    return <result>


Advantages of functions:
1) Code Reusability
2) Readability
3) Maintainability
4) Modularity
'''


# def pizza_maker(topping):
#     print("making a pizza with ", topping)
#     print("adding cheese")
#     print("adding onion")
#     print("baking your pizza")
#     print("here's your ", topping, " pizza\n")

# pizza_maker("mushrooms")
# pizza_maker("chicken")
# pizza_maker("panner")
# pizza_maker("veg")
# pizza_maker("xyz1")
# pizza_maker("xyz2")


# def cube_of_number(num):
#     result = num * num * num
#     return result

# num1 = 2
# c1 = cube_of_number(num1)
# print("cube of the number ", num1, " is ", c1)

# num2 = 3
# c2 = cube_of_number(num2)
# print("cube of the number ", num2, " is ", c2)


'''
# multiple arguments 
'''

# def product_of_two_number(num1, num2):
#     result = num1 * num2

#     return result

# print(product_of_two_number(2, 3))
# print(product_of_two_number(5, 15))

# naming style 
# 1. snake case 
# e.g. product_of_two_number
# 2. camel case
# e.g. productOfTwoNumbers
#  camelCase, ArpanDas
# kabab case
# product-of-two-numbers

'''
# default arguments 
'''

# def default_arguments(num1, num2 = 20, num3= 100):
#     print("num1 : ", num1)
#     print("num2 : ", num2)
#     print("num3 : ", num3)

# default_arguments(10, 12)
# # output:
# # num1 :  10
# # num2 :  12 
# # num3 :  100

# default_arguments(10)
# # output:
# num1 :  10 
# num2 :  20 
# num3 :  100


'''
#keywords of the argument
'''
def keywords_arguments(x, y , z):
    print("x : ", x)
    print("y : ", y)
    print("z : ", z)
    print("\n")

    

# keywords_arguments("first", "second", "third")
# keywords_arguments("third", "first", "second" )

# keywords_arguments("third", "first", z = "second" )

# keywords_arguments(z = "third", x = "first", y =  "second")


'''
#positional arguments 
'''

def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

# print("Case-1:")
# nameAge("Suraj", 27)

# print("Case - 2")
# nameAge(27, "Suraj")


"""
#scope of variable 
1) Local Scope - it is accessable in particular section of your code

2) Global scope - you will be able to access them globaly 
"""


num1 = 10  # you can access this variable globally

def scope_of_variable():
    num2 = 20 # this is your local variable 
    print("inside the function")
    print("I am able to access num1 : ", num1)
    print("I am able to access num2 : ", num2)
    print("function end --------- \n")

scope_of_variable()

print("outside the function")
print("I am able to access num1 : ", num1)
# print("I am able to access num2 : ", num2) # NameError: name 'num2' is not defined





