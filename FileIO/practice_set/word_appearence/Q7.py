# Write a program to count how many times a given word appears in a file.

with open("myfile.txt", "r") as file:

    data = file.read().split()
    occurrence = data.count("Python")
    print(f"Word 'Python' appears {occurrence} times in the file")