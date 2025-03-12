# Logical Operators in Python (and, or, not)

a = 2
b = 4
c = 6

# AND Operator
print("AND Operator:")
print(a < b and b < c)   # True (2 < 4 and 4 < 6)
print(a > b and b < c)   # False (2 > 4 is False, so the whole expression is False)
print(a != b and b >= c) # False (2 != 4 is True, but 4 >= 6 is False)
print(a == 2 and c > b)  # True (2 == 2 and 6 > 4)
print(a <= b and b != c) # True (2 <= 4 is True and 4 != 6 is True)
print()

# OR Operator
print("OR Operator:")
print(a < b or b > c)    # True  (2 < 4 is True, so the whole expression is True)
print(a > b or b > c)    # False (Both 2 > 4 and 4 > 6 are False)
print(a == 2 or c < b)   # True  (2 == 2 is True, so the whole expression is True)
print(a != 2 or b == 4)  # True  (a != 2 is False, but b == 4 is True)
print(a > c or c > b)    # True  (a > c is False, but c > b is True)
print()

# NOT Operator
print("NOT Operator:")
print(not(a < b))  # False (not True is False)
print(not(a > b))  # True  (not False is True)
print(not(a == 2)) # False (not True is False)
print(not(c < b))  # True  (not False is True)
print(not(b != 4)) # True  (not False is True)
print()

# AND and OR Operator Combination
print("AND & OR Combination:")
print(a < b and b > c or a == 5)  
# (True and False) or False → False or False → False

print(a > b and b < c or c == 15)  
# (False and True) or False → False or False → False
print()

# OR and NOT Operator Combination
print("OR & NOT Combination:")
x = True
y = False
print(x or not y)  # True or not False → True or True → True
print(not x or y)  # not True or False → False or False → False
print()

# AND and NOT Operator Combination
print("AND & NOT Combination:")
a = 3
b = 5
print(a < b and not a == 3)  
# True and not True → True and False → False

print(a != b and not b < a)  
# True and not False → True and True → True
print()

# OR, AND, and NOT Operator Combination
print("OR, AND & NOT Combination:")
a = 4
b = 7
c = 10
print(a > b or a < c and not b > c)  
# False or True and not False
# False or True and True
# False or True → True

print(a < b or not (b == 7 and c > b))  
# True or not (True and True)
# True or not True
# True or False → True
print()

# End of Logical Operators Examples
print("All examples executed successfully!")
