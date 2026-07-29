# Check that a type cannot be changed in python
my_list = [12, 31, "Python", "React.js", True, None, "RAG", False]

my_list[2] = "Java"
print(my_list) # Type can be changed because list is mutable


my_tuple = ("Python", "GenAI", 53138, 23.971, True, False, None)
my_tuple[0] = "Java"
print(my_tuple) # TypeError: tuple' object does not support item assignment