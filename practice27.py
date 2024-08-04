# Write a python program using the function to find the Perimeter of rectangle and area of a rectangle.


length = float(input("Enter the length of the rectangle :- "))
width = float(input("Enter the width of the rectangle :- "))

# Perimeter of rectangle
# Formula :- 2(l+w)
def perimeter():
    perimeter = 2 * (length + width)
    print("Perimeter of the rectangle :- ", perimeter)


# Area of a rectangle
# Fromula :- lenght * width
def area():
    area = length * width
    print("Area of the rectangle :- ", area)

# Perimeter called
perimeter()

# Area called
area()