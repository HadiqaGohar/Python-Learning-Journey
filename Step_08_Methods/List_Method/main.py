# METHODS FOR LIST
fruits : list = ["Apple", "Mango", "Banana", "Orange", "Kivi"]

# APPEND: add in list end
fruits.append("Peach")
print("Append")
print(fruits)

# EXTEND: add another list into current list
fruits.extend(["Watermelon", "Cherry"])
print("Extend")
print(fruits)

# INSERT: insert at specific index
fruits.insert(1, "Pineapple")  # Adding "Pineapple" at index 1
print("Insert")
print(fruits)

# POP: remove last element or specific index
fruits.pop()  # Removes last element ("Cherry")
fruits.pop(2)  # Removes element at index 2 ("Mango")
print("Pop")
print(fruits)

# REMOVE: remove specific element
fruits.remove("Apple")  # Removes "Apple"
print("Remove")
print(fruits)

# INDEX: return index position
print("Index")
index_value = fruits.index("Banana")  # Get index of "Banana"
print(f"'Banana' is at index: {index_value}")

# COUNT: count occurrences of an element
print("Count")
watermelon_count = fruits.count("Watermelon")  # Count occurrences of "Watermelon"
print(f"'Watermelon' appears {watermelon_count} time(s) in the list.")

# SORT: arrange elements alphabetically
fruits.sort()
print("Sort")
print(fruits)

# REVERSE: reverse order of elements
fruits.reverse()
print("Reverse")
print(fruits)

# COPY: create a new copy of the list
fruits_copy = fruits.copy()
print("Copy")
print(fruits_copy)

# CLEAR: empty the list
fruits.clear()
print("Clear")
print(fruits)
