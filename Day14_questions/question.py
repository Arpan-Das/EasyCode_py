# Data types (list, set, tuple, string, dict)

# 1. What is the output of:

# a = [1, 2, 3]
# b = a
# b.append(4)
# print(a) #[1, 2, 3, 4]


# 2. What will this print and why?

# t = (1,)
# print(type(t)) #<class 'tuple'>


# 3. Predict the output:

# s = "abc"
# s = s.replace("a", "A")
# print(s) #Abc


# 4. What is the result of:

# x = [0]*3  #[0, 0 , 0]
# x[0] = 5
# print(x) #[5, 0, 0]


# 5. What does this print?

# s = {1, 2, 3, 3}  
# print(len(s)) #3


# 6. What will this display?

# d = {'a':1, 'b':2}
# d2 = d
# d2['a'] = 99
# print(d['a']) #99


# 7. What is the output and why?

# a = [1, 2, 3]
# b = a[:]

# b[0] = 9
# print(a[0], b[0])  #1 9


# 8. Predict output:

# s = "hello"
# print(s[::2]) #hlo


# 9. What will this print?

# tup = (1,2,3)
# try:
#     tup[0] = 0
# except Exception as e:
#     print("1------")
#     print(e)
#     print("2------")
#     print(type(e)._name_)
#     print("3------")


# 10. What happens here?

# lst = [[0]*3]*3
# print(lst)
# # lst = [[ 0 0 0 ]]* 3
# # lst = [[ 0 0 0 ] [ 0 0 0 ] [ 0 0 0 ]]
# lst[0][0] = 1
# print(lst)




# ---

# If — else / conditional pitfalls

# 11. What is printed?

# x = 0
# if x:
#     print("True")
# else:
#     print("False")
# output : False


# 12. What will the following code output?

# a = 10
# if a > 5:
#     if a < 15:
#         print("A")
# else:
#     print("B")
# output : A

# 13. Predict output:

# n = 16
# print("Even" if n%2==0 else "Odd")

# output : Even


# 14. What does this print and why?

# s = ""
# if not s:
#     print("Empty")
# else:
#     print("Non-empty")




# ---

# Loops (for, while) and loop-edge cases

# 15. What will be printed?

# for i in range(5):
#     pass
# print(i)


# 16. What is the output?

# for i in range(2, -3, -1):
#     print(i, end=" ")
# 2 1 0 -1 -2

# 17. Predict the output and explain:
# for i in range(1 4):
# for i in [1,2,3]:
#     for j in [i]:
#         i = 0
# print(i) # 0


# 18. What will this code print?

# i = 1
# while i < 4:
#     print(i)
#     i += 1
# else:
#     print("Done")


# 19. What is the result of:

# for i in range(3):
#     if i == 1:
#         break
# else:
#     print("Completed")
# print("After")


# 20. Predict output:

# numbers = [1,2,3,4]
# for i in numbers:
#     numbers.remove(i)
# print(numbers)




# ---

# Functions (definitions, default args, return, scope)

# 21. What is printed?

# def f(a, b=[]):
#     b.append(a)
#     return b

# print(f(1))
# print(f(2))

# (Identify the bug — code has a syntax error; fix it mentally if needed and answer the behavior.)


# 22. What will be the output?

# def f(x):
#     x = x + [4]
#     return x

# a = [1,2,3]
# print(f(a)) #[1, 2, 3, 4]

# print(a) #[1, 2, 3]



# 23. Predict output:

# def foo():
#     try:
#         return 1
#     finally:
#         return 2

# print(foo())


# 24. What will this display?

# def outer():
#     x = 5
#     def inner():
#         nonlocal x
#         x = 10
#     inner()
#     return x

# print(outer())


# 25. What does this print?

# def add(a, b):
#     return a + b

# print(add("1", 2))


# 26. What is printed and why?

# def f(a, b=0):
#     return a**b

# print(f(2))
# print(f(2, 3))


# 27. Predict output:

# def f(*args):
#     return sum(args)

# print(f())
# print(f(1,2,3))


# 28. What will be printed?

# x = 10
# def change():
#     x = x + 1
# try:
#     change()
# except Exception as e:
#     print(type(e)._name_)