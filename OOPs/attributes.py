class Employee:
    company = "Deloitte" # Class Attribute
    def __init__(self, name, role, salary):
        self.name = name # Object/Instance Attribute
        self.role = role # Object/Instance Attribute
        self.salary = salary # Object/Instance Attribute

e1 = Employee("Zafar Ashfaq", "GenAI Engineer", 1200000)

print(f"Employee Name: {e1.name}")
print(f"Company: {Employee.company}")
print(f"Role: {e1.role}")
print(f"Salary: {e1.salary}")


