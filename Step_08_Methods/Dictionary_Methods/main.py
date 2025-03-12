# Creating a dictionary
student : dict = {
    "name": "Hadiqa",
    "roll_number": 420730,
    "marks": 91,
    "grade": "A"
}

# 📌 Getting all keys
keys = student.keys()
print("Keys:", keys)  # Output: dict_keys(['name', 'roll_number', 'marks', 'grade'])

# 📌 Getting all values
values = student.values()
print("Values:", values)  # Output: dict_values(['Hadiqa', 420730, 91, 'A'])

# 📌 Getting all items (key-value pairs)
items = student.items()
print("Items:", items)  
# Output: dict_items([('name', 'Hadiqa'), ('roll_number', 420730), ('marks', 91), ('grade', 'A')])

# 📌 Using pop() to remove a specific key-value pair
removed_value = student.pop("marks")
print("Removed Value:", removed_value)  # Output: 91
print("Updated Dictionary:", student)  
# Output: {'name': 'Hadiqa', 'roll_number': 420730, 'grade': 'A'}

# 📌 Using popitem() to remove the last inserted item
removed_item = student.popitem()
print("Removed Item:", removed_item)  # Output: ('grade', 'A')
print("Updated Dictionary:", student)  
# Output: {'name': 'Hadiqa', 'roll_number': 420730}

# 📌 Updating the dictionary with new data
student.update({"marks": 98, "subject": "Mathematics"})
print("Updated Dictionary:", student)  
# Output: {'name': 'Hadiqa', 'roll_number': 420730, 'marks': 98, 'subject': 'Mathematics'}

# 📌 Clearing the dictionary
student.clear()
print("Cleared Dictionary:", student)  # Output: {}

