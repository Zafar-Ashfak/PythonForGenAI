# def display(a, b, c, d):
#     print(a, b, c, d)
#
# def main():
#
#     # TypeError: display() takes 4 positional arguments but 5 were given
#     display("Apple", "Banana", "Grapes", "Papaya", "Mango")
#
# main()

def sum_numbers(*args) -> int:
    return sum(args)

def main():
    print(sum_numbers(1, 2, 3, 4, 5))
    print(sum_numbers(1, 2, 3, 4, 5, 6, 7))
    print(sum_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9 , 10))

main()