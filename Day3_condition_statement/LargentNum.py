num1 = 40
num2 = 80
num3 = 30 



if num1 > num2:
    # num1 is greater then num2
    if num1 > num3:
        # num1 is greater then num3
        print("Largest Num: ", num1)
    else:
        # num3 is greater then num1
        print("largets num : ", num3)
else:
    # num2 is greater then num1
    if num2 > num3:
        # num2 is the largest
        print("largest Num: ", num2)
    else:
        # num3 is the largest num
        print("Largest Num:", num3)