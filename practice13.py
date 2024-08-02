# Write a python program to read a number from the user, and check the number is must be greater then 10 and less than 25.

num = int(input("Enter the number (must greater than 10 and less than 25) :- "))

if(num >= 10):
    # inner condition 
    if(num <= 25):
        print("Number is greater than or equal to 10 and less than or equal to 25 :- ", num)
    else:
        print("Number is too large!!!")
else:
    print(num, "is too small!!!")