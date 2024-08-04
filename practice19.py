# Write a python program to display multiplication table from 1 to 10.

i = 1

while i <= 10:
    print("Table", i, ":- ")
    j = 1
    while j <= 10:
        print(i, "x", j, "=", i*j)
        j += 1
    i += 1
    print()