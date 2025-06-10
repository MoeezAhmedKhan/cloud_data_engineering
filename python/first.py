print("Hello World!")

name = "Moeez"
age = 23
height = 5.3

print(type(name))
print(type(age))
print(type(height))

print("Name is :",name, "Age is :",age, "Height is :",height)

# Data Types in Python:
# Integer
# String
# Float
# Boolean
# None

a = None
print(type(a))

# Python is a case sensative language like (a and A) will be different variables

# Find sum of 2 variables
# Comments in python

# Types of operator
# Arthimatic = (+, -, /, *, %, **) => ** its mean power operator like a^b
# Relational = (==, !=, >, <, >=, <=) => these operators can only return bool value
# Assignment = (=, +=, -=, *=, /=, %=, **=)
# Logical = (and, or, not) => it work on boolean value

# Example for logical operator
a = 4
b = 2
print(not False) 
print(not True) 
print(not (a > b))

value1 = True
value2 = True

print("and operator: when both true = ", (value1 and value1))
print("or operator: = ", (value1 or value1))

# Tyoe Conversion and Type casting
# 1. python automatic do type conversion
# 2. when we manual do so it will be type casting

# Type conversion
a = 4
b = 2.16
print(a + b) #Answer will be in floating point number because there is an implicit/automatic type conversion

# Type casting
a = "4"
b = 2
print(int(a) + b) #There is an explicit type conversion

# ----------------------- How can i get input from User------------------------
name = input("Enter name: ")

# WAP to input 2 nunmbers and print their sum
# WAP to find area of square
# WAP to find avg and input 2 floating point numbers : formila a + b / 2
# WAP and print True if a is grater then or equal to b. otherwise print false. 
