text = "Hii, Everyone \nWe are learning File I/O \nusing Java \nI like programming in Java."

with open("practice.txt", "w") as file:
    file.write(f"\n{text}")

with open("practice.txt", "r") as file:
    data = file.read()

new_data = data.replace("Java", "Python")

with open("practice.txt", "a") as append_in_file:
        append_in_file.write(f"\n{new_data}")

with open("practice.txt", "r") as file:
    print(file.read())