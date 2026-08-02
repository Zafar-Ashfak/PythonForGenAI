class Student:
    college = "Maulana Azad National Urdu University, Hyderabad"

    def  __init__(self, name, roll, email, marks):
        self.name = name
        self.roll = roll
        self._email = email
        self._marks = marks

class Details(Student):
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Roll: {self.roll}")
        print(f"College: {self.college}")
        print(f"Email: {self._email}")
        print(f"Marks: {self._marks} CGPA")

def main():
    s1 = Details("Md Anwar Alam", 302113, "Zaidnanhe007@gmail.com", 7.50)
    s1.show_details()

main()