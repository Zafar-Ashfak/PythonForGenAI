try:
    age = int(input("Enter your age: "))
    if age < 0:
        print("You entered an invalid age")
    elif age < 2:
        print("You are an infant")
    elif age < 4:
        print("You are a toddler")
    elif age < 13:
        print("You are a child")
    elif age < 18:
        print("You are a teenager")
    elif age < 39:
        print("You are an adult")
    elif age < 59:
        print("You are a middle age person")
    else:
        print("You are a senior citizen")

except ValueError:
    print("Invalid input for age, please try again!")