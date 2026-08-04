# No Arguments Decorators
from functools import wraps

def greet(func):

    @wraps(func)
    def wrapper():
        print("Good Morning")
        func()
        print("Bye-Bye")
    return wrapper

@greet
def hello():
    print("Hello World!")

def main():
    hello()

main()

