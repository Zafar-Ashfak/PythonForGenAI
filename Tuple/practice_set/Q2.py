marks = list()

marks.append(int(input("Enter the marks of first student: ")))
marks.append(int(input("Enter the marks of second student: ")))
marks.append(int(input("Enter the marks of third student: ")))
marks.append(int(input("Enter the marks of fourth student: ")))
marks.append(int(input("Enter the marks of fifth student: ")))

print(marks)
marks.sort()
print(f"Students marks in sorted manner\n{marks}")