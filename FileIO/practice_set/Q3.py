# Write a program to append a new line of text to an existing file.

message = input("Enter your message: ")

with open("student.txt", "a+") as file:
    file.write(f"\n{message}")