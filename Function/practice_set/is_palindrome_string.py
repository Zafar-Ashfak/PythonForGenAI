# Write a function to check if a user given string is palindrome

def is_palindrome(text):
    lp = 0
    rp = len(text) - 1

    while lp <= rp:
        if text[lp] != text[rp]:
            return False

        lp = lp + 1
        rp = rp - 1

    return True


def main():
    print("Program to check a string is palindrome")
    text = input("Enter a string: ")
    res = is_palindrome(text)
    if res:
        print(f"'{text}' is a palindrome string")
    else:
        print(f"'{text}' is not a palindrome string")


main()