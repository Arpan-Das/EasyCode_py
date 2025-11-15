num = int(input("Enter a number "))
n = 1
for i in range(1, num + 1):
    n*= i
    if i == num:
        print(i)
    else:
        print(i,end="*")

print("The factorial is",n)