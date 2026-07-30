# Write a function that doesn't take any parameters but returns any value.
import math

# Function definition
def circle_area():
    r = int(input("Enter the radius of the circle: "))
    return math.pi * r * r;

def main(): # main function definition
    area = circle_area()
    print(f"Area of the circle is: {area:.2f}")

main() # main function call