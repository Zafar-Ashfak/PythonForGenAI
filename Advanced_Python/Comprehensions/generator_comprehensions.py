# Write a function to print even and odd numbers using generator comprehensions.
print("Program to print even numbers up to n")
n = int(input("Enter a number: "))
evens = (i for i in range(1, n + 1) if i % 2 == 0)

print(f"\nEven numbers from 2 to {n}")
for even in evens:
    print(even, end=" ")

print(f"\n\nOdd numbers from 1 to {n}")
odds = (i for i in range(n) if i % 2 != 0)
for odd in odds:
    print(odd, end=" ")