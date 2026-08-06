def division():
    try:
        n = int(input("Enter the numerator: "))
        d = int(input("Enter the denominator: "))
        res = n / d
        print(f"\n{n} / {d} = {res}")
    except ValueError:
        print("Invalid input, please enter integers!")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    finally:
        print("Execution completed!!")


def main():
    division()

main()
           