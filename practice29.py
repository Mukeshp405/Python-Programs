# Write a function that returns the maximum of two numbers

def max_two(num1, num2):
    if(num1 > num2):
        print(num1, "is greater!!!")
    elif(num2 > num1):
        print(num2, "is greater!!!")
    else:
        print(num1, "and", num2, "both are equal")
    
num1 = int(input("Enter the first number :- "))
num2 = int(input("Enter the second number :- "))
max = max_two(num1, num2)