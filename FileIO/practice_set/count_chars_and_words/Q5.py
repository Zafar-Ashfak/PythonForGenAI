# Write a program to count the total number of words in a file.
with open("file.txt") as file:
    data = file.read()

    words = data.split()

    count = 0
    for word in words:
        count += 1

    # print(f"Total number of words in the file 'file.txt' is: {len(words)}")
    print(f"Total number of words in the file 'file.txt' is: {len(words)}")

