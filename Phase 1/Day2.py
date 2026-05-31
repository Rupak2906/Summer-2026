#Operators
print(5 + 3)  # Addition
print(5 - 3)  # Subtraction
print(5 * 3)  # Multiplication
print(5 / 3)  # Division
print(5 % 3)  # Modulus
print(5 ** 3) # Exponentiation

# Bitwise Operators
print(5 & 3)  # Bitwise AND
print(5 | 3)  # Bitwise OR
print(5 ^ 3)  # Bitwise XOR
print(~5)     # Bitwise NOT
print(5 << 1) # Left Shift
print(5 >> 1) # Right Shift 

# Logical Operators
print(True and False)  # Logical AND
print(True or False)   # Logical OR 
print(not True)        # Logical NOT  

# Comparison Operators
print(5 == 3)  # Equal to
print(5 != 3)  # Not equal to
print(5 > 3)   # Greater than
print(5 < 3)   # Less than
print(5 >= 3)  # Greater than or equal to
print(5 <= 3)  # Less than or equal to    

# Assignment Operators
x = 5
x += 3  # Equivalent to x = x + 3
print(x)  # Output: 8
x -= 2  # Equivalent to x = x - 2
print(x)  # Output: 6
x *= 4  # Equivalent to x = x * 4
print(x)  # Output: 24
x /= 6  # Equivalent to x = x / 6
print(x)  # Output: 4.0 

# Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]   
print(a is b)  # True 
print(a is c)  # False since a and c are different objects in memory and this gives false for List, Dictionary, Set, etc.
print(a == c)  # True since a and c have the same content

# Membership Operators
print(1 in a)  # True
print(4 in a)  # False
print(1 not in a)  # False
print(4 not in a)  # True  