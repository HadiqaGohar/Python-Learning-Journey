#  Identity Operators 

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True (Same memory location)
print(a is c)  # False (Different memory location)
print(a is not c)  # True
