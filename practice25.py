# Write a python program to get the Fibonacci series in between 0 to 50

num1 = 0
num2 = 1

print("Fibonacci series between 0 and 50:")
while num1 <= 50:
    print(num1, end=" ")
    num1, num2 = num2, num1 + num2
