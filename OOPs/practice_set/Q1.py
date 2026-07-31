class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_percentage(self):
        total_marks = sum(self.marks)
        return total_marks / 3

s1 = Student("Jarun Jawed", [98, 80, 92])
print(f"Student Name: {s1.name}")
print(f"You got {s1.get_percentage()}% marks")