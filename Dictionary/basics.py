employee = {
    "id": 201345,
    "name": "Zafar Ashfaq",
    "age": 27,
    "salary": "₹ 10LPA",
    "address": "Tolichowki Hyderabad (Telangana)"
}

print(employee, type(employee))

# ************ DICTIONARY METHODS **************

# len() -> Returns the length of the dict
print(f"Length of the employee dict is: {len(employee)}")

# 1. get() -> Returns the value of a key
print(f"Employee ID: {employee.get('id')}")
print(f"Name: {employee.get('name')}")
print(f"Age: {employee.get('age')}")
print(f"Salary: {employee.get('salary')}")
print(f"Address: {employee.get('address')}")

# 2. Difference between get() method and access []
print(employee.get('name'))
print(employee.get('name2')) # returns None
print(employee["name"])
# print(employee["name2"]) # throw an error because name2 doesn't exist in employee dictionary

# 3. key() -> Returns all keys
print(employee.keys())

# 4. values() -> Returns all values
print(employee.values())

# 5. items() -> Returns all key-value pairs.
print(employee.items())

# 6. update() -> Updates key-value pairs and Add if it doesn't exist.
employee.update(
    {"salary": "₹ 18LPA",
    "Role": "GenAI Engineer"
     },
    )
print(employee)

# 7. pop() -> Removes a key and returns its value.
employee.pop('address')
print(employee)

# 8. popitems() -> Removes the last inserted key-value pair.
employee.popitem()
print(employee)

