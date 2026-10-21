# Python print() Statement
# =======================

# Definition:
# print() is a built-in Python function used to display output on the screen.
# We can use it to display messages, variable values, and calculation results.


# 1. Printing a message
print("Hello, Python!")

# 2. Printing a calculation
print(10 + 20)


# 3. Printing name, age, and city using separate print() statements
print("Name: Bhavitha")
print("Age: 21")
print("City: Mangalore")


# 4. Printing name and age using one print() statement
print("Name: Bhavitha, Age: 21")


# The sep Parameter
# =================
# Definition:
# sep specifies the separator placed between multiple values in print().
# The default separator is a space (" ").

# Printing Python, SQL, and Java separated by a hyphen
print("Python", "SQL", "Java", sep="-")


# The end Parameter
# =================
# Definition:
# end specifies what is printed at the end of a print() statement.
# By default, end is a newline ("\n").
# Using end=" " keeps the next print() output on the same line with a space.

print("Hello", end=" ")
print("Python")


# F-Strings
# =========
# Definition:
# An f-string is a formatted string that lets us insert variables
# and expressions directly inside a string using curly braces {}.
# We write the letter f before the opening quotation mark.

name = "Rahul"
age = 21

print(f"My name is {name} and I am {age} years old.")


# F-String with a Calculation
# ===========================
# We can write an expression inside {} to calculate its value.

a = 10
b = 20

print(f"The sum is {a + b}")