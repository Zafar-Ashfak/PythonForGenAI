from functools import wraps

# Parameter as number Decorator
def addition(func):
    @wraps(func)
    def wrapper(a, b):
        print("Start adding...")
        result = func(a, b)
        print(f"{a} + {b} = {result}")
        print("Finished...")
        return result
    return wrapper

@addition
def get_sum(a, b):
    return a + b

def main():
    # function("Zafar Ashfak")

    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    get_sum(a, b)

main()