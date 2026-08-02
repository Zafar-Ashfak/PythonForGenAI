class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @staticmethod
    def greet():
        print("Hello person!")

    def show_details(self):
        print(f"Person Name: {self.name}")
        print(f"Age: {self.age}")


def main():
    p1 = Person("Zafar Ashfaq", 27)
    p1.greet()
    p1.show_details()

    del p1 # deleting the object
    # UnboundLocalError: cannot access local variable 'p1' where it is not associated with a value

    # p1.greet()
    # p1.show_details()


main()