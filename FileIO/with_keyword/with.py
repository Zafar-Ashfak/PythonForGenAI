langs = "Python, Java, JavaScript, TypeScript, C, C++, Go, Rust, Swift, PHP, Ruby"

with open("programming_lang.txt", "w") as file:
    file.write(langs)

with open("programming_lang.txt", "r") as file:
    data = file.read()
    print(data)