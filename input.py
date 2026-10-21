# Python User Input Practice
# Topic: Taking Input from the User in Python

# What is input()?
# input() is a built-in function used to accept input from the user.
# The input() function always returns a string (str),
# even when the user enters a number.
#
# We can use int() to convert input into an integer
# and float() to convert input into a floating-point number.


# Q1. Input and Display Name
# Accept the user's name and print a welcome message.

name = input("Enter your name: ")
print(f"Welcome, {name}!")


# Q2. Input Name and Age
# Accept the user's name and age.
# Display their values and data types.
# Both values are strings because input() returns str by default.

name = input("Enter your name: ")
age = input("Enter your age: ")

print("Name:", name)
print("Age:", age)
print("Data type of name:", type(name))
print("Data type of age:", type(age))


# Q3. Add Two Numbers
# Accept two integers and print their sum.
# int() converts the input strings into integers.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

total = a + b
print("Sum:", total)


# Q4. Basic Calculator
# Accept two integers and display their sum, difference,
# product, and quotient.
# The / operator performs division and returns a float.
# The second number must not be zero for division.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)

if b != 0:
    print("Quotient:", a / b)
else:
    print("Quotient: Cannot divide by zero")


# Q5. Celsius to Fahrenheit
# Accept temperature in Celsius and convert it to Fahrenheit.
# Formula: F = (C * 9 / 5) + 32
# float() allows the user to enter decimal temperatures.

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Fahrenheit:", fahrenheit)