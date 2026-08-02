class Animal:

    @staticmethod
    def eat():
        print("Animal eat...")

    @staticmethod
    def breathe():
        print("Animal breathe...")

class LandAnimal(Animal):
    def __init__(self, legs):
        self.legs = legs

    def walk(self):
        print(f"Walks on {self.legs} legs")

class WaterAnimal(Animal):
    def __init__(self, fins):
        self.fins = fins

    def swim(self):
        print(f"Swim using {self.fins} fins")


class Turtle(LandAnimal, WaterAnimal):
    def __init__(self, legs, fins):
        LandAnimal.__init__(self, legs)
        WaterAnimal.__init__(self, fins)
    pass

def main():
    tuck = Turtle(4, 2)
    tuck.eat()
    tuck.breathe()
    tuck.walk()
    tuck.swim()

main()