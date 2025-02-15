# Python Data Types - Examples

# String (str)
student = "Hadiqa Gohar"  
print(type(student))  # Output: <class 'str'>

# Integer (int)
rollNumber = 420730  
print(type(rollNumber))  # Output: <class 'int'>

# Float (float)
marks = 90.5  
print(type(marks))  # Output: <class 'float'>

# Boolean (bool)
isPassed = True  
print(type(isPassed))  # Output: <class 'bool'>

# List (list) - Ordered, mutable collection
subjects = ["HTML", "CSS", "Python"]  
print(type(subjects))  # Output: <class 'list'>

# Tuple (tuple) - Ordered, immutable collection
grades = (90, 85, 88)  
print(type(grades))  # Output: <class 'tuple'>

# Set (set) - Unordered, unique values
unique_numbers = {1, 2, 3, 4, 4, 5}  
print(type(unique_numbers))  # Output: <class 'set'>

# Dictionary (dict) - Key-value pairs
student_info = {"name": "Hadiqa", "roll_no": 420730, "marks": 90.5}  
print(type(student_info))  # Output: <class 'dict'>

# NoneType (None) - Represents absence of value
unknown_value = None  
print(type(unknown_value))  # Output: <class 'NoneType'>

# Bytes (bytes)
byte_data = b"Hello"  
print(type(byte_data))  # Output: <class 'bytes'>

# Bytearray (bytearray) - Mutable byte data
mutable_bytes = bytearray(5)  
print(type(mutable_bytes))  # Output: <class 'bytearray'>

# Memoryview (memoryview) - Memory view object
mem_view = memoryview(bytes(5))  
print(type(mem_view))  # Output: <class 'memoryview'>

# Complex Number (complex)
complex_number = 3 + 5j  
print(type(complex_number))  # Output: <class 'complex'>
