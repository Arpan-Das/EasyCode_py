# num=int(input("Enter your number "))
# i=1
# while i<=num:
#     print("*"*i)
#     i+=1

'''
*   line:1 print: 1
**  line:2 print: 2
*** line:3 print: 3
****    line:4 print: 4
*****   line:5 print: 5


*****
****
***
**
*

 * * * * *
  * * * *
   * * *
    * *
     *

num = 4
*       line:1 print:1  
**      line:2 print:2
***     line:3 print:3
****    line:4 print:4
***     line:5 print:3
**      line:6 print:2
*       line:7 print:1

*****
****
***
**
*
**
***
****
*****

'''

num = 4
for i in range(num,0, -1):
    for j in range(1, i+1):
        print("*", end="")    
    print()
    
for i in range(2, num+1):
    for j in range(1, i+1):
        print("*", end="")    
    print()

