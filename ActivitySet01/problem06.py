# Variables, Expressions & Statements

sum=0
count=0
try:
    while True:
        number=input("enter the number :")
        if number=="done":
            break
        sum+=int(number)
        count+=1

    print("The Sum of the enter the number is : ",sum)
    print("total number enter by the user is : ",count)
    print("the average of the given number is : ",sum/count)
except ValueError:
    print("invalid number")