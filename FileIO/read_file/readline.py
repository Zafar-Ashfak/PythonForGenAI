file = open("intro.txt", "r")
# data = file.read()

data = file.read(13) # prints only 10 chars
print(data)

line1 = file.readline() # prints the line 1
# print(line1)

line2 = file.readline() # prints the line 2
# print(line2)

file.close()