my_list = [1, 3, 5.2, 66, 331, "Zafar", "Ashfaq", True, False, None]

print(my_list, type(my_list))

#   ***************** LISTS METHODS *******************

nums = [71, 22, 30, 64, 15]
print(nums)

# 1. append() -> Add val to the end of the list
nums.append(56)
print(nums)

# 2. extend() -> Add all items from an iterable
nums.extend([27, 38, 99])
print(nums)

# 3. insert() -> insert val at given position
nums.insert(3, 990)
print(nums)

# 4. remove() -> Remove the first occurrence from the list
nums.remove(64)
print(nums)

# 5. pop() -> Remove and return item at index i (last item by default)
nums.pop(2)
print(nums)

# 6. count() -> Return number of occurrences from the list
occ = 71
print(f"{occ} occurs {nums.count(occ)} times")

# 7. sort() -> Sort the list in place
nums.sort()
print(nums)

# 8. reverse() -> reverse the list
nums.reverse()
print(nums)

# 9. copy() -> returns a shallow copy of the list
copy_list = nums.copy()
copy_list[2] = 1999
print(nums)
print(copy_list)

# 10. clear() -> Removes all elements from the list
copy_list.clear()
print(copy_list)

# 11. len() -> Returns the length of the list
print(len(nums))

# 12. max() -> Returns the largest val
print(max(2, 13, 21, 6, 19, 7))

# 13. min() -> Returns the smallest val
print(min(2, 13, 21, 6, 19, 7))

# 14. sum() -> Returns the sum of the given numbers
print(sum({2, 13, 21, 6, 19, 7}))
print(sum(nums))

# 15. index() -> Returns the index of the first occurrence
idx = my_list.index(331)
print(idx)

# 16. List Concatenation
list1 = [5, 2, 9, 4, 1, 7, 8, 4]
list2 = [6, 8, 1, 3, 5, 2, 1]

concat_list = list1 + list2
print(concat_list) #

# 17. Membership
print(4 in list1) # True
print(104 in list1) # False

print(202 not  in list2) # True
print(6 not in list2) # False

# 18. Repetition
print([100, 200, 300, ] * 3)


# 19. Slicing -> Returns sliced list
print(list1[0 : 5])
print(list1[0: ])
print(list1[ : 4])
print(list1[::-1])


# 20. List Comprehension (Very Important)
n = 10
squares = [i * i for i in range(1, n + 1)]
print(squares)