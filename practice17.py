# Write a python program to calculate attendance of the student. If his/her attendance is < 75% then student is not allowed to sit in the examination. Read the total number of classes held and attended by the student. Calculate percentage and display allowed to sit or not.

# Refer to the above question and allow the student to sit if he/she has a medical cause. Ask the user if he/she has a medical cause or not.("Y" or "N") and print accordingly.

total_classes_held = int(input("Enter the total number classes held :- "))
classes_attended = int(input("Enter the total number of calsses attended by the student :- "))
medical_cause = str(input("Do you have a medical cause or not? (Y/N) :- "))

if(total_classes_held > 0):
    percentage = (classes_attended / total_classes_held) * 100
else:
    print("Total number of classes held must be greater than 0.")
    exit()

if(medical_cause.lower() == "y"):
    print(f"Your class attended percentage is :- {percentage:.2f}%")
    print("Student are allowed to sit in the examiation due to the medical cause.")
elif(percentage < 75):
    print(f"Your class attended percentage is :- {percentage:.2f}%")
    print("You are not allowed to sit in the examination")
else:
    print(f"Your class attended percentage is :- {percentage:.2f}%")
    print("You are allowed to sit in the examiation")