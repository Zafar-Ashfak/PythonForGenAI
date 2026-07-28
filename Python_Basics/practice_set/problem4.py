import os

path = "/Users/zafaraftab/PythonForGenAI"

contents = os.listdir(path)

print(f"Contents of {path}:\n")

# printing each dir in the given path one by one
for item in contents:
    print(item)