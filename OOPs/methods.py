class Student:
    college = "Indian Institute Of Technology, Mumbai" # Class Attribute
    def __init__(self, name, roll, age, marks): # Constructor
        self.name = name # Object Attribute
        self.roll = roll # Object Attribute
        self.age = age # Object Attribute
        self.marks = marks # Object Attribute

    def show_info(self): # method
        print(f"Student Name: {self.name}")
        print(f"College: {Student.college}")
        print(f"Roll: {self.roll}")
        print(f"Age: {self.age}")
        print(f"marks: {self.marks}")

# Creating objects
s1 = Student("Sidra Fatima", 1, 21, 98.63)
s1.show_info()

