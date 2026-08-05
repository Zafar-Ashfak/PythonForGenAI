# Write a function to print even numbers from 2 to n using generator

def get_even(n):
    for i in range(2, n + 1, 2):
        yield i

def main():
    # even = get_even(100)
    # print(next(even))
    # print(next(even))
    # print(next(even))
    # print(next(even))
    # print(next(even))

    for even in get_even(20):
        print(even)

main()