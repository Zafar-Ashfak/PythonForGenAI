def show_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def main():

    show_profile(id=101, name="Zafar Ashfaq", email="Zafarashfak008@gmail.com", contact="+91 9876543210", age=27)
    print()
    show_profile(id=102, name="Tony Stark", email="Tonystark3000@gmail.com", contact="+91 9234561231", age=29, gender="Male", city="New York")

main()    