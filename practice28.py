# Write a python program to find sum of each digit of given number using function. Like number=1234 then sum = 1+2+3+4

def sum():
    num = int(input("Enter the number :- "))
    ans = 0

    while num > 0:
        rem = num % 10
        ans = ans + rem
        num = num // 10

    print("Sum of number :- ", ans) 

sum()