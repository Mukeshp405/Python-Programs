# Write a program to stop user from withdrawing money more than the available amount balance.

savingAccBalance = 1000

withDrawing = int(input("Enter the amount to withdraw:- "))

if withDrawing > savingAccBalance:
    print("Insufficient Balance!!!")
else:
    print("Withdrawn Successfully!!!")