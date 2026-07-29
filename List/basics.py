my_list = [1, 3, 5.2, 66,331, "Zafar", "Ashfaq", True, False, None]

print(my_list, type(my_list))

#   ***************** LISTS METHODS *******************

num = [71, 22, 30, 64, 15]
print(num)

# 1. append() -> Add val to the end of the list
num.append(56)
print(num)

# 2. extend() -> Add all items from an iterable
num.extend([27, 38, 99])
print(num)

# 3. insert() -> insert val at given position
num.insert(3, 990)
print(num)

# 4. remove() -> Remove the first occurrence from the list
num.remove(64)
print(num)

# 5. pop() -> Remove and return item at index i (last item by default)
num.pop(2)
print(num)

# 6. count() -> Return number of occurrences from the list
occ = 71
print(f"{occ} occurs {num.count(occ)} times")

# 7. sort() -> Sort the list in place
num.sort()
print(num)

# 8. reverse() -> reverse the list
num.reverse()
print(num)

# 9. copy() -> returns a shallow copy of the list
copy_list = num.copy()
print(copy_list)

# 10. clear() -> Removes all elements from the list
copy_list.clear()
print(copy_list)

# 11. len() -> Returns the length of the list
print(len(num))

# 12. max() -> Returns the largest val
print(max(2, 13, 21, 6, 19, 7))

# 13. min() -> Returns the smallest val
print(min(2, 13, 21, 6, 19, 7))

# 14. sum() -> Returns the sum of the given numbers
print(sum({2, 13, 21, 6, 19, 7}))
print(sum(num))

# 15. index() -> Returns the index of the first occurrence
# 16. Membership
# 17. List Concatenation
# 18. Repetition
# 19. Slicing
# 20. List Comprehension (Very Important)
squares = [i * i for i in range(1, 6)]
print(squares)