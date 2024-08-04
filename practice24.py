# Write a Python program that prints all the numbers from 0 to 9 except 4 and 7.

for i in range(10):
    if(i == 4):
        continue
    elif(i == 7):
        continue
    print(i)