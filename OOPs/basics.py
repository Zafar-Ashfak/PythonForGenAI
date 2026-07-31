class Car:

    def __init__(self):
        print("Object is creating....")

    brand = "Ferrari"
    def __init__(self, wheels, color):
      self.wheels = wheels
      self.color = color

# Creating object of class Car
c1 = Car(4, "Red")
print(f"Car Brand: {c1.brand}")
print(f"Color: {c1.color}")
print(f"Wheels: {c1.wheels}")