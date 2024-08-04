# Write a Python program to accept the average percentage of student check the student grade obtained by the student based on the below conditions.
# If marks below 35 then grade is "FAIL"
# If marks are in between 35 and 40(inclusive) then the grade is "PASS"
# If marks are in between 40 and 50(inclusive) then the grade is "HS"
# If marks are in between 50 and 60(inclusive) then the grade is "SC"
# If marks are in between 60 and 75(inclusive) then the grade is "FC"
# Above 75(inclusive) then the grade is "FD"

avg_per = float(input("Enter your average percentage :- "))
print(f"Your Average percentage is :- {avg_per}%")

if(avg_per < 35):
    print("Your grade is FAIL")
elif(avg_per >= 35 and avg_per < 40):
    print("Your grade is PASS")
elif(avg_per >= 40 and avg_per < 50):
    print("Your grade is HS")
elif(avg_per >= 50 and avg_per < 60):
    print("Your grade is SC")
elif(avg_per >= 60 and avg_per <= 75):
    print("Your grade is FC")
elif(avg_per > 75):
    print("Your grade is FD")
else:
    print("Invalid average percentage!!!")