# Write a python program to accept number from the user and calculate the sum of all numbers between 1 and given number by the user.

num = int(input("Enter the number :- "))
sum = 0

# using for loop
# for i in range(1, num+1):
#     sum += i

# using for loop
i = 1
while i <= num:
    sum += i
    i += 1

print("Sum of number between 1 to", num, "is", sum)