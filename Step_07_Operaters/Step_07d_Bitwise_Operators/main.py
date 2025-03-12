# Define numbers for examples
a = 60          # In binary: 0011 1100
b = 13          # In binary: 0000 1101

# AND Operator: Sets bits to 1 if both bits are 1
print("AND Operator:")
print(a & b)     # Output: 12 (binary: 0000 1100)
print()

# OR Operator: Sets bits to 1 if at least one of the bits is 1
print("OR Operator:")
print(a | b)     # Output: 61 (binary: 0011 1101)
print()

# XOR Operator: Sets bits to 1 if only one of the bits is 1
print("XOR Operator:")
print(a ^ b)     # Output: 49 (binary: 0011 0001)
print()

# NOT Operator: Inverts all bits (ones become zeros, and zeros become ones)
print("NOT Operator:")
print(~a)        # Output: -61 (binary: 1100 0011, using two's complement representation)
print()

# Left Shift Operator: Shifts bits to the left by specified number of positions
print("Left Shift Operator:")
print(a << 2)    # Output: 240 (binary: 1111 0000)
print()

# Right Shift Operator: Shifts bits to the right by specified number of positions
print("Right Shift Operator:")
print(a >> 2)    # Output: 15 (binary: 0000 1111)
print()
