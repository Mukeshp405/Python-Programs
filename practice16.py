# Write a python program to calculate attendance of the student. If his/her attendance is < 75% then student is not allowed to sit in the examination. Read the total number of classes held and attended by the student. Calculate percentage and display allowed to sit or not.

classes_held = int(input("Enter the total number of classes held :- "))
classes = int(input("Enter the total number of classes attended by the student :- "))

if(classes_held > 0):
    percentage = (classes / classes_held) * 100
else:
    print("Total number of classes held must be greater than 0")
    exit()

if(percentage < 75):
    print(f"Your class attended percentage is :- {percentage:.2f}%")
    print("You are not allowed to sit in the examination")
else:
    print(f"Your class attended percentage is :- {percentage:.2f}%")
    print("Your are allowed to sit in the examination")