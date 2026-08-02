class Car:
    def __init__(self, name, color, fuel_type):
        self.name = name
        self.color = color
        self.fuel_type = fuel_type

    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped...")

class SuperCar(Car):
    def __init__(self, name, color, fuel_type, speed):
        super().__init__(name, color, fuel_type)  # Calling parent constructor
        self.speed = speed
        super().start() # Calling parent method

    def performance(self):
        print(f"{self.name} top speed is: {self.speed}")


def main():
    ferrari = SuperCar("Ferrari", "Red", "Diesel", 340)
    ferrari.performance()
    ferrari.stop()

main()
