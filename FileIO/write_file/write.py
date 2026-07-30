text = "Hii, I am Md Ashfaq Alam. And I am a junior GenAI Engineer."

file = open("demo.txt", "w")
file.write(text)
file.close()

demo_file = open("demo.txt", "r")
data = demo_file.read()
print(data)
file.close()