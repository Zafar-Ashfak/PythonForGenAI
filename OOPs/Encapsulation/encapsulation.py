class Student:
    college = "Indian Institute Of Technology, Bombay"

    def __init__(self, name, roll, program, department, cpi, hostel, web_email):
        self.name = name
        self.roll = roll
        self.program = program
        self.department = department
        self.cpi = cpi
        self.hostel = hostel
        self.web_email = web_email

    @staticmethod
    def welcome():
        print("Welcome! We are thrilled to have you with us this term.")
        print("All course materials, schedules, and announcements are now live on portal. Stay curious, work hard, and don't hesitate to reach out if you need guidance along the way.")
        print("Wishing you a productive and successful semester ahead!")

    def show_details(self):
        print(f"Student Name: {self.name}")
        print(f"Roll: {self.roll}")
        print(f"Program: {self.program}")
        print(f"Department: {self.department}")
        print(f"College: {Student.college}")
        print(f"CPI: {self.cpi}")
        print(f"Hostel: {self.hostel}")
        print(f"Web Email: {self.web_email}")


def main():
    s1 = Student("Bruce Wayne", 210050042, "B.Tech", "Computer Science & Engineering", 9.15, "Hostel 16", "bruce.wayne@iitb.ac.in")
    s1.show_details()
    print("\n\n")
    s1.welcome()


main()