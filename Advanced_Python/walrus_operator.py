# name =  input("Enter your name: ")
# if name.isalpha():
#     print(f"Hello, {name}")
# else:
#     print("Invalid input, Please try again!")

# Walrus Operator :=
# if (name := input("Enter your name: ")).isalpha():
#     print(f"Good Morning, {name}")
# else:
#     print("Invalid input, please try again!")
#

while (text := input("Enter a text: (type exit to quit): ")) != "exit":
    print(f"Entered text: {text}")


# def is_eligible():
#     if (age := int(input("Enter your age: "))) < 18:
#         print(f"You are {age} years old, and you are not eligible to vote")
#     else:
#         print(f"You are {age} years old, and you are eligible to vote")
#
# def main():
#     is_eligible()
#
# main()