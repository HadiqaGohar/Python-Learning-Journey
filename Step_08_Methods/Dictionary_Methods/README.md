### 📌 Python Dictionary Methods – Simple & Easy Guide  

A **dictionary** in Python is a collection of key-value pairs. This guide covers useful methods to access, modify, and manage dictionary data efficiently.  

#### 🔹 Creating a Dictionary  
A dictionary stores related data using **keys** and **values**:  
```python
student = {
    "name": "Hadiqa",
    "roll_number": 420730,
    "marks": 91,
    "grade": "A"
}
```  

#### 🔹 Accessing Data  
- **Get all keys**: `student.keys()` → 📌 Returns `['name', 'roll_number', 'marks', 'grade']`  
- **Get all values**: `student.values()` → 📌 Returns `['Hadiqa', 420730, 91, 'A']`  
- **Get all key-value pairs**: `student.items()` → 📌 Returns all dictionary items  

#### 🔹 Modifying the Dictionary  
- **Remove a specific key-value pair** using `.pop()`  
  ```python
  student.pop("marks")
  ```
  📌 Removes `"marks": 91`  

- **Remove the last added item** using `.popitem()`  
  ```python
  student.popitem()
  ```
  📌 Removes the last key-value pair  

- **Update or add new values** using `.update()`  
  ```python
  student.update({"marks": 98, "subject": "Mathematics"})
  ```
  📌 Adds `"subject": "Mathematics"` and updates `"marks": 98`  

- **Clear all dictionary data** using `.clear()`  
  ```python
  student.clear()
  ```
  📌 Removes all items, leaving an empty dictionary `{}`  

💡 **Dictionaries are powerful!** They help organize data efficiently, making them a key part of Python programming. 🚀
