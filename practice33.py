# Write a python program to find the index of the first occurance of a substring in a string.

str = input("Enter the string :- ")
sub_str = input("Enter the substring :- ")

ans = str.find(sub_str)

if(ans != -1):
    print(f"The substring '{sub_str}' is found at index {ans}")
else:
    print(f"The subsstring '{sub_str}' is not found in the string")
