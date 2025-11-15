'''
2. WRITE A function to compute the sum of the first n terms of the following series, 
S = 1 - 2 + 3 - 4 + 5 - 6 …………… n

'''


n=int(input("Enter your number "))
sum=0
for i in range (1,n+1):
    if i%2==0:
      sum-=i
    else:
      sum+=i
print(sum)