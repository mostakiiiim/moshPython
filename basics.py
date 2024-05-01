"""Python Basics"""

# Variables
age = 14
salary = 14.5

bank = 212

# Dynamic Typing
"""
Python is a dynamically typed language, which means that you don't have to declare the type of a variable
when you create one. It will run in the runtime

"""
student_count = 14
print(type(student_count))

# Type annotation
"mypy uses type annotations to check the types of variables"
age: int = 15
age = "Fifteen"

print(age)
"mypy will give error for the above code"

# Mutable and Immutable Types
'Built in primitive types such as numbers, strings, boolean are immutable '

x = 1

print(id(x))

'If we change the value of x then the address will also change'

x += 1

print(id(x))

'But lists are mutable thus showing same memory address even after changing the value of list'

y = [1, 3, 4, 5]

print(id(y))

y.append(6)

print(id(y))
# String
# Escape Sequences
# Formatted Strings
# Useful String Methods
# Numbers
# Arithmetic Operators
# Working with Numbers
# Type Conversions
# Logical Operators
# Ternary Operators
# For Loop
# For..Else
# While Loops
# Functions
# Argument--Xargs
# Argument--Xxargs
# Scope
# Debugging
# Exercise
