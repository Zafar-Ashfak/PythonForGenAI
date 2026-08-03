# def display(a, b, c, d):
#     print(a, b, c, d)
#
# def main():
#
#     # TypeError: display() takes 4 positional arguments but 5 were given
#     display("Apple", "Banana", "Grapes", "Papaya", "Mango")
#
# main()

# There would be no TypeError
def display(*args):
    for item in args:
        print(item)

def show(normal, *args):
    print(normal)
    for item in args:
        print(f"\t{item}")

def main():
    fruits = ("Apple", "Banana", "Grapes", "Papaya", "Mango", "Pine apple", "Coconut")
    # display(*fruits)
    show("Fruits Name: ", *fruits)
main()
