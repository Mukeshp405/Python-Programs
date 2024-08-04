# Write a python program to accept a list of numbers as an input from user and perform addition of them and print reslut.

input_Number = input("Enter a list element separated by comma :- ")
list = input_Number.split(',')
print("Calculating sum of element of input list")
sum = 0
for num in list:
    sum += int(num)

print("Sum of Numbers :- ", sum)