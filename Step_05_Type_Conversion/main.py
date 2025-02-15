# Type Conversion

# Number to String

value1 = 10
print(type(value1))
# Ans  : <class 'int'>

valueStr = str(value1)
print(type(valueStr))
# Ans  : <class 'str'>

# String to Number

# Example 1

# value2 = "Helloworld"
# print(type(value2))
# # Ans  : <class 'str'>

# valueInt = int(value2)
# print(type(valueInt))
# Ans  : <class 'int'> Traceback (most recent call last): Error

# Example 2

# value3 = "10"
# print(type(value3))
# # Ans  : <class 'str'>

# valueInt = int(value3)
# print(type(valueInt))
# Ans  : <class 'int'> Traceback (most recent call last): Error

# Boolean to Number

value4 = True
print(type(value4))
# Ans  : <class 'bool'>

valueInt = int(value4)
print(type(valueInt))
# Ans  : <class 'int'>

# Number to Boolean

value5 = 1
print(type(value5))
# Ans  : <class 'int'>

valueBool = bool(value5)
print(type(valueBool))
# Ans  : <class 'bool'>

# String to Boolean

value6 = "True"
print(type(value6))
# Ans  : <class 'str'>

valueBool = bool(value6)
print(type(valueBool))
# Ans  : <class 'bool'>

# Boolean to String

value7 = True
print(type(value7))
# Ans  : <class 'bool'>

valueStr = str(value7)
print(type(valueStr))
# Ans  : <class 'str'>

# String to List

value8 = "Hello"
print(type(value8))
# Ans  : <class 'str'>

valueList = list(value8)
print(type(valueList))
# Ans  : <class 'list'>

# List to String

value9 = ["H", "e", "l", "l", "o"]
print(type(value9))
# Ans  : <class 'list'>

valueStr = str(value9)
print(type(valueStr))
# Ans  : <class 'str'>

# List to Tuple

value10 = ["H", "e", "l", "l", "o"]
print(type(value10))
# Ans  : <class 'list'>

valueTuple = tuple(value10)
print(type(valueTuple))
# Ans  : <class 'tuple'>


# Tuple to List

value11 = ("H", "e", "l", "l", "o")
print(type(value11))
# Ans  : <class 'tuple'>

valueList = list(value11)
print(type(valueList))
# Ans  : <class 'list'>

# List to Set

value12 = ["H", "e", "l", "l", "o"]
print(type(value12))
# Ans  : <class 'list'>

valueSet = set(value12)
print(type(valueSet))
# Ans  : <class 'set'>


# Set to List

value13 = {"H", "e", "l", "l", "o"}
print(type(value13))
# Ans  : <class 'set'>

valueList = list(value13)
print(type(valueList))
# Ans  : <class 'list'>

# List to Dictionary

value14 = [["Name", "John"], ["Age", 25]]
print(type(value14))
# Ans  : <class 'list'>

valueDict = dict(value14)
print(type(valueDict))
# Ans  : <class 'dict'>

# Dictionary to List

value15 = {"Name": "John", "Age": 25}
print(type(value15))
# Ans  : <class 'dict'>

valueList = list(value15)
print(type(valueList))
# Ans  : <class 'list'>

# Dictionary to Tuple

value16 = {"Name": "John", "Age": 25}
print(type(value16))
# Ans  : <class 'dict'>

valueTuple = tuple(value16)
print(type(valueTuple))
# Ans  : <class 'tuple'>

# Tuple to Dictionary

value17 = ("Name", "John"), ("Age", 25)
print(type(value17))
# Ans  : <class 'tuple'>

valueDict = dict(value17)
print(type(valueDict))
# Ans  : <class 'dict'>

# Set to Dictionary

# value18 = {"Name", "John", "Age", 25}
# print(type(value18))
# # Ans  : <class 'set'>

# valueDict = dict(value18) # Error
# print(type(valueDict))
# # Ans  : Traceback (most recent call last): Error

# Dictionary to Set

value19 = {"Name": "John", "Age": 25}
print(type(value19))
# Ans  : <class 'dict'>

valueSet = set(value19)
print(type(valueSet))
# Ans  : <class 'set'>

# String to Dictionary

# value20 = "Name:John, Age:25"
# print(type(value20))
# # Ans  : <class 'str'>

# valueDict = dict(value20) # Error
# print(type(valueDict))
# # Ans  : <class 'dict'> Traceback (most recent call last): Error

# Dictionary to String

value21 = {"Name": "John", "Age": 25}
print(type(value21))
# Ans  : <class 'dict'>

valueStr = str(value21)
print(type(valueStr))
# Ans  : <class 'str'>

# String to Tuple

value22 = "Name", "John", "Age", 25
print(type(value22))
# Ans  : <class 'tuple'>

valueTuple = tuple(value22)
print(type(valueTuple))
# Ans  : <class 'tuple'>

# Tuple to String

value23 = ("Name", "John", "Age", 25)
print(type(value23))
# Ans  : <class 'tuple'>

valueStr = str(value23)
print(type(valueStr))
# Ans  : <class 'str'>

# String to Set

value24 = "Hello"
print(type(value24))
# Ans  : <class 'str'>

valueSet = set(value24)
print(type(valueSet))
# Ans  : <class 'set'>

# Set to String

value25 = {"H", "e", "l", "l", "o"}
print(type(value25))
# Ans  : <class 'set'>

valueStr = str(value25)
print(type(valueStr))
# Ans  : <class 'str'>

# String to List

value26 = "Hello"
print(type(value26))
# Ans  : <class 'str'>

valueList = list(value26)
print(type(valueList))
# Ans  : <class 'list'>

# List to String

value27 = ["H", "e", "l", "l", "o"]
print(type(value27))
# Ans  : <class 'list'>

valueStr = str(value27)
print(type(valueStr))
# Ans  : <class 'str'>

# String to none

# value28 = "Hello"
# print(type(value28))
# # Ans  : <class 'str'>

# valueNone = None(value28) # Error
# print(type(valueNone))
# # Ans  : <class 'NoneType'> Traceback (most recent call last): Error

# None to String

value29 = None
print(type(value29))
# Ans  : <class 'NoneType'>

valueStr = str(value29)
print(type(valueStr))
# Ans  : <class 'str'>

# None to Number

# value30 = None
# print(type(value30))
# # Ans  : <class 'NoneType'>

# valueInt = int(value30) # Error
# print(type(valueInt))
# # Ans  : <class 'int'> # Traceback (most recent call last): Error

# None to Boolean

value31 = None
print(type(value31))
# Ans  : <class 'NoneType'>

valueBool = bool(value31)
print(type(valueBool))
# Ans  : <class 'bool'>

# None to List

# value32 = None
# print(type(value32))
# # Ans  : <class 'NoneType'>

# valueList = list(value32) # Error
# print(type(valueList))
# # Ans  : <class 'list'> # Traceback (most recent call last): Error

# None to Tuple

# value33 = None
# print(type(value33))
# # Ans  : <class 'NoneType'>

# valueTuple = tuple(value33) # Error
# print(type(valueTuple))
# # Ans  : <class 'tuple'> # Traceback (most recent call last): Error

# None to Set

# value34 = None
# print(type(value34))
# # Ans  : <class 'NoneType'>

# valueSet = set(value34) # Error
# print(type(valueSet))
# # Ans  : <class 'set'> # Trackback (most recent call last)

# None to Dictionary

# value35 = None
# print(type(value35))
# # Ans  : <class 'NoneType'>

# valueDict = dict(value35) # Error
# print(type(valueDict))
# # Ans  : <class 'dict'> # Trackback (most recent call last)

# None to String

value36 = None
print(type(value36))
# Ans  : <class 'NoneType'>

valueStr = str(value36)
print(type(valueStr))
# Ans  : <class 'str'>

#  Number to None

# value37 = 12
# print(type(value37))
# # Ans : <class 'int'>

# valueNone = None(value37)
# print(type(valueNone))
# # Ans : ❌ TypeError

# Float to None

# value38 = 12.44
# print(type(value38))
# # Ans : <class 'float'>

# valueNone = None(value38)
# print(type(valueNone))
# # Ans : ❌ TypeError

#  Integer to String

# value39 = 12.44
# print(type(value39))
# # Ans : <class 'float'>

# valueStr = str(value39)
# print(type(valueNone))
# # Ans : ❌ TypeError

# Float to String

# value40 = "10abc"
# print(type(value40))
# # Ans : <class 'str'>

# valueNone = float(value40)
# print(type(valueNone))
# # Ans : ❌ TypeError


