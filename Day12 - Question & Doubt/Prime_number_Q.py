''''
4. Write a function to find whether a given no. is prime or not. 

A prime number is a natural number greater than 1 that has only two distinct
positive divisors: 1 and itself.

For example, 5 is a prime number because it can only be divided evenly by 1 and 5. 
Numbers greater than 1 that have more than two divisors are called composite numbers 
(e.g., 4 has factors 1, 2, and 4). The number 1 is neither prime nor composite. 


conditoin to be a prime number 
1) greater than 1
2) two distinct positive divisors: 1 and itself
e.g. num = 5 
2 , 3, 4


e.g. 
num 6
2, 3, 4, 5

num = 9 
2, 3, 4, 5, 6, 7, 8
   

'''

print("Program to check the prime number.")

num = int(input("Enter your number: "))
is_prime = True
if num > 1:
    for i in range(2, num):
        print("check i : ", i)
        if num % i == 0:
            print("not prime")
            is_prime = False
            break

if is_prime == True:
    print("Entered number : ", num, " is prime number.")
else:
    print("Entered number : ", num, " is not prime number.")





