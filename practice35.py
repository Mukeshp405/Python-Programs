# Write a python program to accept a list of string from the user and print result.

name_list = input("Enter family members name separated by comma :- ")

string_list = name_list.split(',')

for name in string_list:
    print(name)