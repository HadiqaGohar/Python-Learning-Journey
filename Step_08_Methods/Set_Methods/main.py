# Creating a set of vegetables
vegetables = {"carrot", "lettuce", "onion", "radish", "tomato"}

# 📌 add() - Adds a single element to the set
vegetables.add("potato")
print("After add():", vegetables)

# 📌 update() - Adds multiple elements at once
vegetables.update(["cucumber", "eggplant", "garlic"])
print("After update():", vegetables)

# 📌 remove() - Removes a specific element (throws an error if the element is missing)
vegetables.remove("lettuce")
print("After remove():", vegetables)

# 📌 discard() - Removes a specific element (NO error if the element is missing)
vegetables.discard("radish")
print("After discard():", vegetables)

# 📌 pop() - Removes a **random** element
removed_item = vegetables.pop()
print(f"Removed item: {removed_item}")
print("After pop():", vegetables)

# Creating another set for comparison
vegetables2 = {"carrot", "lettuce", "onion", "radish", "tomato"}

# 📌 difference() - Returns elements present in one set but not in the other
different = vegetables.difference(vegetables2)
print("Difference:", different)

# 📌 intersection() - Returns common elements in both sets
common = vegetables.intersection(vegetables2)
print("Intersection:", common)

# 📌 union() - Combines both sets (removes duplicates)
all_vegetables = vegetables.union(vegetables2)
print("Union:", all_vegetables)

# 📌 clear() - Removes all elements from the set
vegetables.clear()
print("After clear():", vegetables)  # Output: set()
