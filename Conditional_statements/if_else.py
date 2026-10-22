# ============================================================
# PYTHON IF-ELSE STATEMENTS
# ============================================================
# Definition:
# An if-else statement is a conditional statement in Python
# that allows a program to make decisions based on conditions.
#
# If the condition is True, the if block executes.
# If the condition is False, the else block executes.
#
# Syntax:
#
# if condition:
#     statement
# else:
#     statement
#
# Important rules:
# 1. Use the if keyword to check a condition.
# 2. Use a colon (:) after if and else.
# 3. Indentation is required inside both blocks.
# 4. The else block executes when the if condition is False.
# 5. Use comparison operators such as ==, !=, >, <, >=, <=.
# 6. Use and when both conditions must be True.
# 7. Use or when at least one condition must be True.
# 8. The % operator returns the remainder after division.
# ============================================================


# Q1. Check whether a number is Even or Odd
# A number is even if it is divisible by 2 without a remainder.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Q2. Check voting eligibility
# A person aged 18 or above is eligible to vote in this example.

age = int(input("Enter age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")


# Q3. Check whether a student has passed or failed
# Assume 35 is the minimum passing mark.

marks = int(input("Enter marks: "))

if marks >= 35:
    print("Pass")
else:
    print("Fail")


# Q4. Understand falsy values
# In Python, zero is a falsy value.
# Therefore, the if block will not execute.

x = 0

if x:
    print("yes")
else:
    print("no")  # Output: no


# Q5. Understand truthy values
# A non-empty string is truthy, even if it contains the word "False".
# The string "False" is not the Boolean value False.

name = "False"

if name:
    print("yes")  # Output: yes
else:
    print("no")


# Q6. Find the largest of two numbers

a = 10
b = 25

if a > b:
    print("Largest:", a)
else:
    # If a is not greater than b, b is the largest or equal.
    print("Largest:", b)  # Output: Largest: 25


# Q7. Check whether a number is positive, negative, or zero
# Positive numbers are greater than zero.
# Negative numbers are less than zero.

num = int(input("Enter a value: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    # Handle zero separately instead of incorrectly printing Negative.
    print("Zero")


# Q8. Find the smallest of two numbers

a = 10
b = 25

if a < b:
    print("Smallest:", a)  # Output: Smallest: 10
else:
    # This block executes when a is greater than or equal to b.
    print("Smallest:", b)


# Q9. Check whether a character is a vowel using lower()
# lower() converts uppercase letters to lowercase before checking.

ch = "A"

if ch.lower() in "aeiou":
    print("Vowel")
else:
    print("Not a vowel")

# Output: Vowel
# Explanation: 'A'.lower() becomes 'a'.


# Q10. Check whether a character is a vowel without lower()
# Include both lowercase and uppercase vowels in the string.

ch = "A"

if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Not a vowel")

# Output: Vowel
# Explanation: Both uppercase and lowercase vowels are included.


# Q11. Check whether a year is a leap year
# A leap year is divisible by 4 but not by 100,
# unless it is also divisible by 400.
#
# and: Both conditions must be True.
# or: At least one condition must be True.

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

# Examples:
# 2024 -> Leap year
# 1900 -> Not a leap year
# 2000 -> Leap year


# Q12. Check whether a list is empty
# An empty list [] is falsy.
# A list containing one or more items is truthy.

items = []

if items:
    print("Have items")
else:
    print("Empty cart")  # Output: Empty cart


# Q13. Check whether a character is a vowel or consonant
# Assumption: The input must be exactly one English alphabet letter.
# lower() converts the input to lowercase.

ch = input("Enter a character: ").lower()

if ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")

# Example:
# Input: b
# Output: Consonant
# Note: This example assumes valid alphabetic input.


# Q14. Check whether a number is divisible by both 3 and 5
# A number is divisible by both if both remainders are zero.
# The and operator requires both conditions to be True.

n = int(input("Enter a number: "))

if n % 3 == 0 and n % 5 == 0:
    print("Divisible by both")
else:
    print("Not divisible by both")

# Example:
# Input: 15
# Output: Divisible by both


# Q15. Basic username and password check
# Both the username and password must match.
# This is a learning example, not secure authentication.
# Never store real passwords directly in source code.

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid username or password")


# Q16. Check whether a character is uppercase
# isupper() returns True if the string contains uppercase
# cased characters and no lowercase cased characters.

ch = input("Enter a character: ")

if ch.isupper():
    print("Uppercase")
else:
    print("Not uppercase")

# Example:
# Input: A
# Output: Uppercase


# Q17. Check whether a character is a digit
# isdigit() returns True if all characters in a non-empty
# string are digits.

ch = input("Enter a character: ")

if ch.isdigit():
    print("Digit")
else:
    print("Not a digit")

# Example:
# Input: 7
# Output: Digit

