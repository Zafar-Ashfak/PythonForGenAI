class Animal:
    def __init__(self, name, color, legs, breed):
        self.name = name
        self.color = color
        self.legs = legs
        self.breed = breed

    @staticmethod
    def eat():
        print("Animal eats...")

    @staticmethod
    def breathe():
        print("Animal breathes.")

class Horse(Animal):
    def __init__(self, name, color, legs, breed):
        super().__init__(name, color, legs, breed)


    @staticmethod
    def eat():
        print("Eats grass, husk, and grain.")


class Mustang(Horse):
    def __init__(self, name,  color, legs, breed, strength):
        super().__init__(name, color, legs, breed)
        self.strength = strength

    def show_details(self):
        print(f"Animal name: {self.name}")
        print(f"Color: {self.color}")
        print(f"Legs: {self.legs}")
        print(f"Breed: {self.breed}")
        print(f"Strength: {self.strength}")

def main():
    m1 = Mustang("Horse", "Dark brown", 4, "American Mustang", "Strongest")
    m1.show_details()
    m1.eat()
    m1.breathe()

main()