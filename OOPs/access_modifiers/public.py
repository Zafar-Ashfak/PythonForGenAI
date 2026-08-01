class Car:
    wheels = 4
    def __init__(self, brand, model, year, color, fuel_type):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.fuel_type = fuel_type


def main():
    c1 = Car("Lamborghini", "Aventador", 2026, "Green", "Petrol")
    print(f"Car brand: {c1.brand}")
    print(f"Model: {c1.model}") #  Variables are accessible outside the class
    print(f"Year: {c1.year}")
    print(f"Color: {c1.color}")
    print(f"Wheels: {Car.wheels}")
    print(f"Fuel type: {c1.fuel_type}")

main()