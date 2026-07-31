# Write a program to create a file named student.txt and write your name, age, and city into it.
# And read the entire contents of a file and print them on the screen.
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

with open("student.txt", "w") as file:
    file.write(f"Student Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"city: {city}")


with open("student.txt", "r") as file:
    print(file.read())