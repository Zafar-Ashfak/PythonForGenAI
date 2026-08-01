class Signup:
    def __init__(self, username, email, password):
        self.username = username
        self.__email = email
        self.__password = password

    def get_email(self):
        return self.__email

    def set_email(self, email):
        if '@' in email and '.' in email:
            self.__email = email
            print("Email updated successfully!")
        else:
            print("Invalid email address!")

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        if len(new_password) < 8:
            print("Password must be at least 8 characters long")
        else:
            self.__password = new_password
            print("Password updated successfully!")


def main():
    s1 = Signup("Zafar Ashfak", "Zafarashfak008@gmail.com", "IamGroot@008")
    print(f"Username: {s1.username}")
    print(f"Email: {s1.get_email()}")
    print(f"Password: {s1.get_password()}")


    print("\nUpdating email and password")
    s1.set_email("Zafarashfak007@zohomail.in")
    s1.set_password("IamProgrammer@008")
    print(f"Email: {s1.get_email()}")
    print(f"Password: {s1.get_password()}")

main()