my_tuple = (82, 2.92, "Python", True, False, None)
print(my_tuple)

# *********** TUPLE METHODS *************

nums = (3, 1, 7, 3, 4, 9, 2, 6, 5, 1, 4)
print(f"First element of the tuple is: {nums[0]}")
print(f"Last element of the tuple is: {nums[len(nums) - 1]}")
print(f"Middle element of the tuple is: {nums[len(nums) // 2]}")

# 1. count() -> Returns the number of times a value appears in the tuple.
val1 = 3
val2 = 5
print(f"Element {val1} appears {nums.count(val1)} times in the tuple")
print(f"Element {val2} appears {nums.count(val2)} times in the tuple")

# 2. index() -> Returns the index of the first occurrence of a value.
idx = nums.index(9)
print(f"Element 9 is at index: {idx}")

# 3. len() -> Returns length of the tuple
print(f"Length of the tuple is: {len(nums)}")

# 4. Tuple Slicing
print(nums[2: 5])
print(nums[0: ])
print(nums[ : 6])
print(nums[0 : 7: 2])
print(nums[::-1])

# 5. Element access
fruits = ("Apple", "Mango", "Grapes", "Banana", "Papaya", "Pine apple")
print(fruits[2])
print(fruits[4])

# 6. Concatenation
tuple1 = (2, 4, 6, 8, 10)
tuple2 = (3, 6, 9, 12, 15)
print(tuple1 + tuple2)

# 7. Repetition
print((200, 500) * 3)
print(("Hello Zafar", ) * 5)

# 8. Convert the tuple to list
my_list = list(nums)
print(my_list)
my_list.sort()
print(my_list)
print(my_list.count(1))
my_list.reverse()
print(my_list)

# Here my_list is sorted in descending order
# 9. Convert the list back to tuple
new_tuple = tuple(my_list)
print(new_tuple)


