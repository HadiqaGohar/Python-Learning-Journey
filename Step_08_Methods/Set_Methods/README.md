### 🥦 Python Set Methods – Easy Guide  

A **set** in Python is an **unordered collection** of unique items. Here’s how to manipulate sets using built-in methods.  

#### 🔹 Creating a Set  
A set stores **unique** elements without duplicates:  
```python
vegetables = {"carrot", "lettuce", "onion", "radish", "tomato"}
```  

#### 🔹 Adding Elements  
- **`add()`** – Adds a single element to the set  
  ```python
  vegetables.add("potato")
  ```  
  📌 Set after adding: `{"carrot", "lettuce", "onion", "radish", "tomato", "potato"}`  

- **`update()`** – Adds multiple elements at once  
  ```python
  vegetables.update(["cucumber", "eggplant", "garlic"])
  ```  
  📌 Set after update: `{"carrot", "lettuce", "onion", "radish", "tomato", "potato", "cucumber", "eggplant", "garlic"}`  

#### 🔹 Removing Elements  
- **`remove()`** – Deletes a specific element **(throws an error if missing)**  
  ```python
  vegetables.remove("lettuce")
  ```  

- **`discard()`** – Deletes a specific element **(NO error if missing)**  
  ```python
  vegetables.discard("radish")
  ```  

- **`pop()`** – Removes a **random** element  
  ```python
  removed_item = vegetables.pop()
  ```  
  📌 Since sets are unordered, any random element might be removed.  

#### 🔹 Set Operations  
- **`difference()`** – Returns elements in one set but not in another  
  ```python
  vegetables.difference(vegetables2)
  ```  

- **`intersection()`** – Returns elements **common** in both sets  
  ```python
  vegetables.intersection(vegetables2)
  ```  

- **`union()`** – Combines both sets **(removes duplicates)**  
  ```python
  all_vegetables = vegetables.union(vegetables2)
  ```  

#### 🔹 Clearing the Set  
- **`clear()`** – Removes all elements  
  ```python
  vegetables.clear()
  ```  
  📌 Set after clear: `set()`  

💡 **Sets are great for eliminating duplicates and performing mathematical operations efficiently! 🚀**
