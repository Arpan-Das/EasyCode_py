'''
3. Write a function that checks whether a given string is Palindrome
 or not. Use this functionto find whether the string entered by user
 is Palindrome or not.

 what is palindrome?
 its a string which same when you read it from starting or end
 e.g.  aba, abcba, 121, 12321

'''

# str = "abcdef"
str = "acdgbgcca"

def check_palindrom(str):
    length = len(str)
    for i in range(0, length // 2):
        # print("start", str[i])

        # print("end i = ", i, " and ch =", str[ - (i + 1)])
        print("Comparing ", str[i], " with ", str[-(i + 1)])
        if str[i] != str[ - (i + 1)]:
            return False
    
    return True 

status = check_palindrom(str)
print(status)
if status == True:
    print("Given string:", str, " is a palindrom.")
else:
    print("Given string:", str, " is not a palindrom.")


"""


"""




