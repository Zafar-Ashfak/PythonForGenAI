# no-argument generator to print num from 1 to 1000 but resumes for the next call
def nums():
    for num in range(1, 1000):
        yield num


# argument generator to print num from 1 to n but resumes for the next call
def nums_up_to(n):
    for i in range(1, n + 1):
        yield i

# no argument generator but yield many statements
def fruits():
    yield "Apple"
    yield "Banana"
    yield "Water melon"
    yield "Melon"
    yield "Orange"
    yield "Papaya"
    yield "Jack fruit"


def main():
   # num = nums()
   # print(next(num))
   # print(next(num))
   # print(next(num))
   # print(next(num))
   # print(next(num))

   # num = nums_up_to(10)
   # print(next(num))
   # print(next(num))
   # print(next(num))
   # print(next(num))
   # print(next(num))

   for fruit in fruits():
       print(fruit)

main()