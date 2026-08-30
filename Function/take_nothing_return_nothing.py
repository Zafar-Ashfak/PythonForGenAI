# Write a function that neither takes any parameters nor returns any value.

# Function definition
def addition():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(f"{num1} + {num2} = {num1 + num2}")

def main(): #  main function definition
    addition() # function call


main()  # main function call