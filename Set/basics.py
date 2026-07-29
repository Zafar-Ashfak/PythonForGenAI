my_set = {1, 3, 9, 4, 2, 7, 3, 2, 1}
print(my_set) # Prints collection of unique values in unordered manner
print(type(my_set))

print(f"Length of the set is: {len(my_set)}") # returns the length of unique elements

# **************** SET METHODS ******************

nums = {10, 20, 30, 40}
print(nums)

# 1. add() -> adds a single element
nums.add(50)
print(nums)

# 2. update() -> Adds multiple elements
nums.update({70, 80, 90})
print(nums)

# 3. remove() -> removes an existing element otherwise throw an error
nums.remove(70)
print(nums)

# 4. discard() -> Removes an element if it exists.
nums.discard(40)
nums.discard(1294)
print(nums)

# 5. pop() -> Removes and returns a random element.
removed_element = nums.pop()
print(f"Removed element: {removed_element}")
print(nums)

# 6. copy() -> create a shallow copy of the set
new_nums = nums.copy()
print("Copied set")
print(new_nums)

# 7. union() -> Combines two sets and remove duplicates.
set1 = {1, 2, 3, 4, 5}
set2 = {3, 5, 7, 9}

print(set1.union(set2))
print(set1 | set2)

# 8. intersection() -> Returns common elements
print(set1.intersection(set2))
print(set1 & set2)

# 9. difference() -> Returns elements present only in the first set
print(set1.difference(set2))

# 10. symmetric_difference() ->  Returns elements that are in either set, but not both.
print(set1.symmetric_difference(set2))

# 11. Create an empty set
# empty_set = {} # creates an empty dict
empty_set = set()
print(type(empty_set))


# Convert a list to a set
new_list = [1, 4, 8, 3, 4, 6, 4, 1, 7, 8, 6]
new_set = set(new_list)
print(new_list)
print(new_set)

# Convert a set to a list
numbers = { 1, 2, 4, 5, 3 }
new_numbers = list(numbers)
print(numbers)
print(new_numbers)







