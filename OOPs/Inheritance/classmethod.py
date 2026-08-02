class Person:
    name = "Anonymous"

    # def change_name(self, new_name):
    #     # self.name = new_name # Cannot change class attribute
    #     self.__class__.name = new_name # This property can class attribute

    @classmethod
    def change_name(cls, new_name):
        cls.name = new_name

def main():
    p1 = Person()
    p1.change_name("Clark Kent")
    print(p1.name) # Calling class attribute using object
    print(Person.name) # Calling class attribute using class itself

main()
