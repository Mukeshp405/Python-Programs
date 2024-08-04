# Write a function called show_stars(rows). If rows is 5, it should print the following:
# *
# * *
# * * *
# * * * *
# * * * * *

def show_stars(rows):
    print("Pyramid of", rows, "is :- ")
    print()
    for i in range(1, rows):
        for j in range(i):
            print("*", end=" ")
        print()

num = int(input("Enter the number :- "))
show_stars(num)
