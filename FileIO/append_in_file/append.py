text = input("Enter a data: ")

with open("demo.txt", "a") as file:
    file.write(f"\n{text}")

with open("demo.txt", "r") as file:
    data = file.read()
    print(data)
