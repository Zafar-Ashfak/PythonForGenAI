# Write a program to detect double space in a string. And remove the double space.
sentence = "Hii, I am          a GenAI Engineer."
print(sentence)

print(f"White space occurs at index: {sentence.find("  ")}")
new_str = sentence.replace("          ", " ")
print(new_str)


