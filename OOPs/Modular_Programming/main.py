import addition, subtraction

def abstraction(num1, num2):
    addition.add(num1, num2)
    subtraction.sub(num1, num2)

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    abstraction(num1, num2)

main()

