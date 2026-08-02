class Car:
    def __init__(self, brand, model, color, fuel_type):
        self.brand = brand
        self.model = model
        self.color = color
        self.fuel_type = fuel_type

    def start(self):
        print(f"{self.brand} {self.model} started...")

    def stop(self):
        print(f"{self.brand} {self.model} stopped...")

class SuperCar(Car):
    def __init__(self, brand, model, color, fuel_type, speed):
        super().__init__(brand, model, color, fuel_type)
        self.speed = speed

    def get_speed(self):
        print(f"Super car speed is: {self.speed} km/h")

def main():
    s1 = SuperCar("Lamborghini", "Aventador", "Green", "Petrol", 240)
    s1.start()
    s1.get_speed()
    s1.stop()

main()