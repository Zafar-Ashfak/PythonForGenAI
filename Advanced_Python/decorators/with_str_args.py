from functools import wraps

# Parameter as String Decorator
def greet(func):
    @wraps(func)
    def wrapper(name):
        print("Start...")
        func(name)
        print("End...")
    return wrapper


@greet
def function(name):
    print("Hello,", name)

def main():
    function("Zafar Ashfak")

main()