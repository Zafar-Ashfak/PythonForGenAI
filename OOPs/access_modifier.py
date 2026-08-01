class Signin:
    def __init__(self, email, password):
        self.email = email
        self.__password = password

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        if len(new_password) < 8:
            print("Password must be at least 8 characters long")
        else:
            self.__password = new_password
            print("Password updated successfully!")

def main():
    s1 = Signin("Zafarashfak008@gmail.com", "IamGroot@008")
    print(s1.email)
    print(s1.get_password())

    s1.set_password("IamProgrammer@008")
    print(s1.get_password())

main()