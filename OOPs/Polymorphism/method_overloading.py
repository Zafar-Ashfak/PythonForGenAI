class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def show_number(self):
        return f"{self.real} + {self.img}i"

    def __add__(self, num2):
        new_real = self.real + num2.real
        new_img = self.img + num2.img
        return Complex(new_real, new_img)

    def __sub__(self, num2):
        new_real = self.real - num2.real
        new_img = self.img - num2.img
        return Complex(new_real, new_img)


def main():
    num1 = Complex(3, 9)
    print(f"Num1: {num1.show_number()}")

    num2 = Complex(1, 4)
    print(f"Num2: {num2.show_number()}")

    # num3 = num1.add(num2) # We are adding two Complex number by calling the add method

    num3 = num1 + num2 # We want to add two Complex number like this, so we will have to make add method dunder
    print(f"Sum: {num3.show_number()}")

    # num4 = num1.sub(num2)
    num4 = num1 - num2
    print(f"Difference: {num4.show_number()}")


main()
