class Student:
    college = "Indian Institute Of Technology, Bombay"

    def __init__(self, name, roll, marks): # Constructor
        self.name = name
        self.roll = roll
        self.marks = marks

    @staticmethod
    def welcome():
        print("Welcome students")

    def show_info(self): # Method
        print(f"Student Name: {self.name}")
        print(f"College: {Student.college}")
        print(f"Roll: {self.roll}")
        print(f"Marks: {self.marks}")

def main():
    s1 = Student("Tony Stark", 13, 95.76)
    s1.welcome()
    s1.show_info()


main()
