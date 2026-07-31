# Write a program to convert all the text in a file to uppercase and save it back to the same file.

with open("python.txt", "r") as file:
    data = file.read().upper()

with open("python.txt", "a") as file:
    file.write(f"\n{data}")
    print("Convert text into uppercase successfully")