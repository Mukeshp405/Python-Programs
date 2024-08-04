# Write a Python program to read number from user and make it reverse. Example no = 458 reverse no = 854

num = int(input("Enter the number (more than 1 digit) :- "))
ans = 0

while num > 0:
    rem = num % 10
    ans = ans * 10 + rem
    num = num // 10

print("Reverse Number :-", ans)

