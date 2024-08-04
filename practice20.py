# Write a python program to print the following pattern
# *
# * *
# * * *
# * * * *

# using while loop
# i = 0
# while i < 6:
#     j = 0
#     while j < i:
#         print('*', end=" ")
#         j += 1
#     i += 1
#     print()

num = int(input("Enter the number :- "))
# using for loop
for i in range(num):
    # print start
    for j in range(i):
        print("*", end=" ")
    print()