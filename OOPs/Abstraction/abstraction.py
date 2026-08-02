from abc import ABC, abstractmethod
import math

class Shape2D(ABC):

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

class Shape3D(ABC):

    @abstractmethod
    def surface_area(self) -> float:
        pass

    @abstractmethod
    def volume(self) -> float:
        pass

class Circle(Shape2D):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive")

        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


class Square(Shape2D):
    def __init__(self, side: float):
        if side <= 0:
            raise ValueError("Side must be positive")

        self.side = side

    def area(self) -> float:
        return self.side ** 2

    def perimeter(self) -> float:
        return 4 * self.side

class Cube(Shape3D):
    def __init__(self, side: float):
        if side <= 0:
            raise ValueError("Side must be positive")

        self.side = side

    def surface_area(self) -> float:
        return 6 * (self.side ** 2)


    def volume(self) -> float:
        return self.side ** 3

def main():
    cir1 = Circle(10)
    print(f"Area of the circle is: {cir1.area():.2f}")
    print(f"Perimeter of the circle is: {cir1.perimeter():.2f}")

    print()

    sq = Square(4)
    print(f"Area of the square is: {sq.area()}")
    print(f"Perimeter of the square is: {sq.perimeter()}")

    print()

    cb = Cube(8)
    print(f"Total surface area of the cube is: {cb.surface_area()}")
    print(f"Volume of the cube is: {cb.volume()}")

main()
