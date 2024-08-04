# A company decided to give a bonus of 10% to the employee if his/her year of service to more than 5 years. Ask the user for their basic salary and year of service and print the net bonus amount.

salary = float(input("Enter your salary :- "))
year = int(input("Enter the year of service :- "))

if (year > 5):
    bonus = salary * 0.10
    print("your salary is :-", salary)
else:
    bonus = 0
    print("You will not get any bonus!!!")

print(f"Net bonus amount :- ${bonus:.2f}")