class Employee:
    company = "Google"
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def show_details(self):
        print(f"Company: {self.company}")
        print(f"Role: {self.role}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary} LPA")

class Engineer(Employee):
    def __init__(self, name, age, role, department, salary):
        super().__init__(role, department, salary)
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Age: {self.age}")
        super().show_details()
        print()


def main():
    e1 = Engineer("Md Ashfak Alam", 27, "AI Engineer", "IT", 2300000)
    e1.show_details()

main()