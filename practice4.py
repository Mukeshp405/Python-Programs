# Accept two numbers from user and perform swapping of two numbers

num1 = int(input("Enter the first number:- "))
num2 = int(input("Enter the second number:- "))

print("first number:- ", num1)
print("second number:- ", num2)

temp = num1 
num1 = num2
num2 = temp

print("first number:- ", num1)
print("second number:- ", num2)