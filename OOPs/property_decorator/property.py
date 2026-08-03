class Student:
    college = "Indian Institute Of Technology, Delhi"
    def __init__(self, name, phy, che, math):
        if not all(0 <= mark <= 100 for mark in (phy, che, math)):
            raise ValueError("Marks must be between 0 and 100")

        self.name = name
        self.phy = phy
        self.che = che
        self.math = math
        # self.percentage = str((phy + che + math) / 3) + "%"

    # def get_percentage(self): # It is way to change value of the attribute
    #     return str((self.phy + self.che + self.math) / 3) + "%"

    @property
    def percentage(self):
        return (self.phy + self.che + self.math) / 3

def main():
    phy = int(input("Enter your physics marks: "))
    che = int(input("Enter your chemistry marks: "))
    math = int(input("Enter your math marks: "))
    s1 = Student("Jarun Jawed", phy, che, math)
    print(f"Student Name: {s1.name}")
    print(f"Physics marks: {s1.phy}, Chemistry marks: {s1.che}, Math marks: {s1.math}")
    print(f"Score: {s1.percentage} %")
    print("By mistake teacher gave physics 98, it should be 89")
    s1.phy = 89
    print(f"Physics new marks: {s1.phy}")
    print(f"Score: {s1.percentage} %")

main()