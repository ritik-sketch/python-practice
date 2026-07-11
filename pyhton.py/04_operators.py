'''
#arithmetic operators
# Variables
print("arithmetic operators")
a = 15
b = 4

# Addition
print("Addition:", a + b)  

# Subtraction
print("Subtraction:", a - b) 

# Multiplication
print("Multiplication:", a * b)  

# Division
print("Division:", a / b) 

# Floor Division
print("Floor Division:", a // b)  

# Modulus
print("Modulus:", a % b) 

# Exponentiation
print("Exponentiation:", a ** b)
print('\n')


#comparison operators
print("comparison operators")
a = 13
b = 33

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
print("\n")


#logical operators
print("logical operators ") #logical and , logical not, logical or
a = True
b = False
print(a and b)
print(a or b)
print(not a)
print("\n")

#bitwise
print("bitwise operators") #and,shift,not,xor,or
a = 10
b = 4

print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)
print("\n")

#Assignment Operators
#This operator is used to assign the value of the right side of 
# the expression to the left side operand.
print("Assignment Operators")
a = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)
print("\n")

#Identity Operator
print("Identity Operator")
a = 10
b = 20
c = a

print(a is not b)
print(a is c)
print("\n")

#membership operators
#in & not_in are the membership operators in python 
print("membership operators")
x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")
print("\n")


#Ternary Operator 
print("Ternary Operator ")
a, b = 10, 20
min = a if a < b else b

print(min)
print("\n")
'''

num1 = "5"
num2 = 3
result = num1 * num2
print(result)
