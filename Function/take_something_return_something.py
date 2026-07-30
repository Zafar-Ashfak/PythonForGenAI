# Write a function that takes any parameters and returns a value.

# Function definition
def rectangle_area(length, width):
    area = length * width
    return area

def main(): # main function definition
    l = int(input("Enter the length of the rectangle: "))
    w = int(input("Enter the width of the rectangle: "))
    area = rectangle_area(l, w) # function call
    print(f"Area of the rectangle is: {area}")

main() # main function call