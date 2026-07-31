with open("myfile.txt", "r") as file:
    # count = 0

    # for line in file:
    #     count += 1

    count = len(file.readlines())
    print(f"The total number of lines in the file 'myfile.txt' is: {count}")
