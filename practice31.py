# Write a function for checking the speed of drivers. This function should have one parameter: speed. If speed is less than 70, It should print "OK". Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: "Points:2". If the driver gets more than 12 points, the function should print: "License suspended". 

def check_speed(speed):
    speed_limit = 70

    if(speed < speed_limit):
        print("OK")
    else:
        excess_speed = speed - speed_limit
        demerit_points = excess_speed // 5

        if(demerit_points > 12):
            print("License suspended!!!")
        else:
            print(f"Points: {demerit_points}")

speed = float(input("Enter the speed :- "))
check_speed(speed)