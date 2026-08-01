from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def volume(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Area of the circle is: {(math.pi * (self.radius ** 2)):.2f}")

    def volume(self):
        print("Circle has no volume")
    def perimeter(self):
        print(f"Perimeter of the circle is: {(2 * math.pi * self.radius):.2f}")

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print(f"Area of the square is: {self.side ** 2}")
    def volume(self):
        print(f"Square has no volume")

    def perimeter(self):
        print(f"Perimeter of the square is: {4 * self.side}")

class Cube(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print(f"Total surface area of the cube is: {6 * (self.side ** 2)}")

    def volume(self):
        print(f"Volume of the cube is: {self.radius ** 3}")
    def perimeter(self):
        print(f"Perimeter of the cube is: {12 * self.side}")

def main():
    cir1 = Circle(10)
    cir1.area()
    cir1.volume()
    cir1.perimeter()

    print()

    sq = Square(4)
    sq.area()
    sq.volume()
    sq.perimeter()

    print()

    cb = Cube(8)
    cb.area()
    cb.volume()
    cb.perimeter()


main()
