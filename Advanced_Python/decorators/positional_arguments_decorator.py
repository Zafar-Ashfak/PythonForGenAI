# positional arguments decorator
from functools import wraps

def addition(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Running...")
        return func(*args, **kwargs)
    return wrapper

@addition
def sum_of_nums(*args, **kwargs):
    return sum(args)


def main():
    res = sum_of_nums(1, 2, 3, 4, 5)
    print(res)

main()
