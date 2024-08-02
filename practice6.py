# Write a python program to read temperature in Celsius and convert to Fahrenheit and Fahrenheit to Celsius
# Formula for temprature conversion :- Celsius = (Fahrenheit - 32) * 5/9
#                                      Fahrenheit = (Celsius * 9/5) + 32

fahrenheit = float(input("Enter the Fahrenheit :- "))

celsius = (fahrenheit - 32) * 5/9

print("Fahrenheit to Celsius :-", celsius)

celsius1 = float(input("Enter the Celsius :- "))

fahrenheit1 = (celsius1 * 9/5) + 32

print("Celsius to Fahrenheit :- ", fahrenheit1)
