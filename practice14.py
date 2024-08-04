# Write a python program to accept values of length and breadth of a rectangle from the user and check if it is square or not.

length = int(input("Enter the length of rectangle :- "))
breadth = int(input("Enter the breadth of rectangle :- "))

if(length == breadth):
    print("The rectangle is a square.")
else:
    print("The rectangle is not a square.")