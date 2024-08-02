# Write a python program to accept a number from the user and check whether the number is divisible by 2 or 3 or not.

num = int(input("Enter the number :- "))

if(num %2 == 0):
    print("Number is divisible by 2")
elif(num %3 == 0):
    print("Number is divisible by 3")
else:
    print("Number is not divisible by 2 and 3")