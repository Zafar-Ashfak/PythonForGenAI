# Iterate on list iterable

nums = [10, 50, 30, 20, 60, 80, 40, 90]

iterator = iter(nums)

while True:
    try:
        num = next(iterator)
        print(num, end=" ")
    except StopIteration:
        break

print()

#********************************************************************************************************
# Iterate on tuple iterable

my_tuple = (1, 2, 7, 3, 9, 4, 5, 8, 6, 2, 4, 7)
it = iter(my_tuple)

while True:
    try:
        print(next(it), end=" ")
    except StopIteration:
        break

print()

#********************************************************************************************************

# Iterate on dict iterable
animals = {
    1: "Cat",
    2: "Dog",
    3: "Camel",
    4: "Cow",
    5: "Goat"
}

dict_itr = iter(animals.items())
while True:
    try:
        print(next(dict_itr))
    except StopIteration:
        break

print()
#********************************************************************************************************

# Creating our Iterator
class Count:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            value = self.current
            self.current += 1
            return value
        raise StopIteration

counter = Count(5)

for num in counter:
    print(num, end=" ")
