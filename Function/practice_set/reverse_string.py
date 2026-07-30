# Write a function to reverse a given string

def reverse(text):
    return text[::-1]


def reversestring(text):
    rev = ""
    for ch in text:
        rev = ch + rev

    return rev

def main():
    print("Program to reverse a given string")
    text = input("Enter a string: ")
    # res = reverse(text)
    res = reversestring(text)
    print(res)

main()