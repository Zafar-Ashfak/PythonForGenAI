# Write a program to count the total number of characters in a file.

with open("file.txt", "r") as file:
    data = file.read()

    # print(len(data))
    count = 0
    for ch in data:
        count += 1

    print(f"Total number of characters in the file 'file.txt' is: {count}")


