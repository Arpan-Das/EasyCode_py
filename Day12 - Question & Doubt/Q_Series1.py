'''
1. WRITE A function to compute the sum of the first n terms of the
following series,
S = 1/1 + 1/2 + 1/3 + 1/4 + …… + 1/n

e.g. n = 3
s = 1/1 + 1/2 + 1/3 


n = 5 
s = 1/1 + 1/2 + 1/3 + 1/4 + 1/5


'''

n = int(input("Enter your number : "))
sum = 0

for i in range(1, n+1):
    sum = sum + 1/i
    # or
    # sum += 1/i

print("Sum of first ", n , " numbers is : ", sum)
print("Sum of first ", n , " numbers is ( round of to 2 decimal point) : ", round(sum,2))


# n = 1.87
# print(round(n))

# n = 1.34
# print(round(n))

# # 1.32 ~ 1

# n = 1.5259 
# print(round(n, 3))

# n = 1.526 
# print(round(n, 2))

# n = 1.53
# print(round(n, 1))





